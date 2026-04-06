#!/usr/bin/env python3
"""
Pull SEC filings for a company and save as markdown in the journal.

Usage:
    python scripts/pull_filings.py META
    python scripts/pull_filings.py META --years 5
    python scripts/pull_filings.py META --forms 10-K,10-Q
    python scripts/pull_filings.py META --years 3 --forms 10-K,10-Q,8-K

Defaults: last 3 years, forms: 10-K, 10-Q, 8-K (earnings-related only)
         Auto-detects foreign private issuers and uses 40-F/20-F/6-K instead
Output:  journal/companies/<TICKER>/filings/
"""

import argparse
import os
import sys
from datetime import datetime, timedelta
from pathlib import Path

from edgar import set_identity, Company

# SEC requires identification
set_identity("Investor Brain investor@example.com")

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOURNAL_DIR = PROJECT_ROOT / "journal"


def get_quarter(date_str: str) -> str:
    """Convert a date to quarter label."""
    month = int(date_str.split("-")[1])
    q = (month - 1) // 3 + 1
    year = date_str.split("-")[0]
    return f"{year}-Q{q}"


def is_earnings_related(filing) -> bool:
    """Check if an 8-K is earnings-related (items 2.02 or 9.01). 6-Ks are always kept."""
    form = filing.form.replace("/A", "")  # Handle amendments
    if form == "6-K":
        return True  # 6-Ks are quarterly/material reports for foreign issuers, keep all
    if form != "8-K":
        return True
    if not filing.items:
        return False
    items = filing.items if isinstance(filing.items, str) else str(filing.items)
    return "2.02" in items or "9.01" in items


def filing_filename(filing) -> str:
    """Generate a clean filename for a filing."""
    form = filing.form.replace("/", "-")
    date = str(filing.filing_date)
    year = date[:4]

    if form in ("10-K", "40-F", "20-F"):
        return f"{form}_{year}.md"
    elif form == "10-Q":
        quarter = get_quarter(str(filing.period_of_report or date))
        return f"10-Q_{quarter}.md"
    elif form == "6-K":
        return f"6-K_{date}.md"
    elif form == "8-K":
        items = filing.items or "general"
        if "2.02" in str(items):
            quarter = get_quarter(date)
            return f"8-K_earnings_{quarter}_{date}.md"
        else:
            return f"8-K_{date}.md"
    else:
        return f"{form}_{date}.md"


def pull_filing_markdown(filing) -> str | None:
    """Extract markdown from a filing. Returns None on failure."""
    try:
        md = filing.markdown()
        if md and len(md) > 100:
            return md
    except Exception as e:
        print(f"  Warning: Could not extract markdown: {e}")

    # Fallback to text
    try:
        txt = filing.text()
        if txt and len(txt) > 100:
            return txt
    except Exception:
        pass

    return None


def build_filing_header(filing) -> str:
    """Build a metadata header for the filing markdown."""
    lines = [
        f"# {filing.form} — {filing.company}",
        f"",
        f"**Filed:** {filing.filing_date}",
        f"**Period:** {filing.period_of_report or 'N/A'}",
        f"**Accession:** {filing.accession_no}",
        f"**SEC URL:** {filing.filing_url}",
    ]
    if filing.items:
        lines.append(f"**Items:** {filing.items}")
    lines.append("")
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def create_filings_index(ticker: str, filings_dir: Path, saved_files: list[dict]):
    """Create an index.md for the filings directory."""
    lines = [
        f"# {ticker} SEC Filings",
        "",
        f"**Last pulled:** {datetime.now().strftime('%Y-%m-%d')}",
        f"**Total filings:** {len(saved_files)}",
        "",
    ]

    # Group by form type
    by_form = {}
    for f in saved_files:
        form = f["form"]
        if form not in by_form:
            by_form[form] = []
        by_form[form].append(f)

    for form in ["10-K", "40-F", "20-F", "10-Q", "6-K", "8-K"]:
        if form not in by_form:
            continue
        lines.append(f"## {form}")
        lines.append("")
        for f in sorted(by_form[form], key=lambda x: x["date"], reverse=True):
            lines.append(f"- [{f['filename']}]({f['filename']}) — Filed {f['date']}, Period {f['period']}")
        lines.append("")

    # Any other forms
    for form, files in by_form.items():
        if form in ["10-K", "40-F", "20-F", "10-Q", "6-K", "8-K"]:
            continue
        lines.append(f"## {form}")
        lines.append("")
        for f in sorted(files, key=lambda x: x["date"], reverse=True):
            lines.append(f"- [{f['filename']}]({f['filename']}) — Filed {f['date']}")
        lines.append("")

    index_path = filings_dir / "index.md"
    index_path.write_text("\n".join(lines))
    print(f"  Created {index_path.relative_to(PROJECT_ROOT)}")


def main():
    parser = argparse.ArgumentParser(description="Pull SEC filings into the journal")
    parser.add_argument("ticker", help="Stock ticker (e.g., META, AAPL)")
    parser.add_argument("--years", type=int, default=3, help="How many years back to pull (default: 3)")
    parser.add_argument("--forms", default=None, help="Comma-separated form types (default: auto-detect)")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    cutoff_date = datetime.now() - timedelta(days=args.years * 365)

    # Resolve company
    try:
        company = Company(ticker)
        print(f"Pulling filings for {ticker}")
        print(f"  Company: {company.name} (CIK: {company.cik})")
    except Exception as e:
        print(f"Error: Could not find company '{ticker}': {e}")
        sys.exit(1)

    # Auto-detect foreign private issuer
    if args.forms:
        forms = [f.strip() for f in args.forms.split(",")]
    else:
        # Check if company files 10-K (domestic) or 40-F/20-F (foreign)
        has_10k = len(company.get_filings(form="10-K")) > 0
        if has_10k:
            forms = ["10-K", "10-Q", "8-K"]
        else:
            has_40f = len(company.get_filings(form="40-F")) > 0
            has_20f = len(company.get_filings(form="20-F")) > 0
            if has_40f:
                forms = ["40-F", "6-K"]  # Canadian issuers
                print("  Detected: Foreign private issuer (40-F/6-K)")
            elif has_20f:
                forms = ["20-F", "6-K"]  # Other foreign issuers
                print("  Detected: Foreign private issuer (20-F/6-K)")
            else:
                forms = ["10-K", "10-Q", "8-K"]  # Fallback

    print(f"  Forms: {', '.join(forms)}")
    print(f"  Since: {cutoff_date.strftime('%Y-%m-%d')}")
    print()

    # Create output directory
    filings_dir = JOURNAL_DIR / "companies" / ticker / "filings"
    filings_dir.mkdir(parents=True, exist_ok=True)

    saved_files = []
    total_skipped = 0

    for form in forms:
        print(f"\n  Fetching {form} filings...")
        try:
            filings = company.get_filings(form=form)
        except Exception as e:
            print(f"  Error fetching {form}: {e}")
            continue

        count = 0
        for filing in filings:
            # Date filter
            filing_date = str(filing.filing_date)
            if datetime.strptime(filing_date, "%Y-%m-%d") < cutoff_date:
                break  # Filings are sorted newest-first

            # For 8-K, only keep earnings-related
            if form == "8-K" and not is_earnings_related(filing):
                continue

            filename = filing_filename(filing)
            filepath = filings_dir / filename

            # Skip if already exists
            if filepath.exists():
                total_skipped += 1
                continue

            print(f"    Pulling {form} {filing_date}...", end=" ", flush=True)

            md = pull_filing_markdown(filing)
            if md is None:
                print("FAILED (no content)")
                continue

            # Add header and save
            content = build_filing_header(filing) + md
            filepath.write_text(content)

            size_kb = len(content) / 1024
            print(f"OK ({size_kb:.0f} KB)")

            saved_files.append({
                "form": form,
                "date": filing_date,
                "period": str(filing.period_of_report or "N/A"),
                "filename": filename,
                "size_kb": size_kb,
            })
            count += 1

        print(f"  {form}: {count} new filings saved")

    if total_skipped:
        print(f"\n  Skipped {total_skipped} already-downloaded filings")

    # Create index
    if saved_files or any((filings_dir / f).exists() for f in os.listdir(filings_dir) if f.endswith(".md")):
        # Rebuild index from all files on disk
        all_files = []
        for f in filings_dir.iterdir():
            if f.name == "index.md" or not f.name.endswith(".md"):
                continue
            # Parse form type from filename
            form = f.name.split("_")[0]
            # Read date from file header
            content = f.read_text()
            date_line = [l for l in content.split("\n") if l.startswith("**Filed:**")]
            date = date_line[0].replace("**Filed:**", "").strip() if date_line else "unknown"
            period_line = [l for l in content.split("\n") if l.startswith("**Period:**")]
            period = period_line[0].replace("**Period:**", "").strip() if period_line else "N/A"
            all_files.append({
                "form": form,
                "date": date,
                "period": period,
                "filename": f.name,
                "size_kb": f.stat().st_size / 1024,
            })
        create_filings_index(ticker, filings_dir, all_files)

    print(f"\nDone. {len(saved_files)} filings saved to {filings_dir.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
