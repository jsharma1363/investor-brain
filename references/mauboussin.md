# Mauboussin Frameworks

Michael Mauboussin's quantitative frameworks for business analysis and valuation.
These complement the Buffett/Munger qualitative frameworks with rigorous, formula-driven tools.

## Core Formulas

### Value Creation
```
ROIC = NOPAT / Invested Capital
ROIC = NOPAT Margin x Capital Turnover
Economic Profit = (ROIC - WACC) x Invested Capital
Value = NOPAT(1 - g/ROIC) / (WACC - g)
```
When ROIC = WACC, growth neither creates nor destroys value. Only when ROIC > WACC does
growth create value. When ROIC < WACC, growth DESTROYS value.

### Owner Earnings / NOPAT Adjustments
```
NOPAT = EBIT(1-t) + Amortization of acquired intangibles (add-back)
Invested Capital = Total Debt + Total Equity - Excess Cash
Excess Cash ~ 2% of sales (rest is excess)
```
For ROIC on organic business (ex-M&A): subtract goodwill from invested capital.
Including goodwill tells you about returns on total capital deployed including M&A premiums.

### ROIIC (Return on Incremental Invested Capital)
```
ROIIC = (Year1 NOPAT - Year0 NOPAT) / (Year0 Invested Capital - Year-1 Invested Capital)
```
Smooth over 3-5 years to reduce noise. ROIIC is forward-looking — it tells you what each
new dollar of investment earns. This is the single most important number for assessing
whether growth creates value.

### Cash Conversion Cycle (Balance Sheet Moat)
```
CCC = DSO + DIO - DPO
DSO = [(Beg AR + End AR)/2] / (Sales/365)
DIO = [(Beg Inv + End Inv)/2] / (COGS/365)
DPO = [(Beg AP + End AP)/2] / (COGS/365)
```
Negative CCC companies (like Amazon at -33 days) use supplier financing to fund growth.

### WACC
```
WACC = (D/V) x kd x (1-t) + (E/V) x ke
```
Prefer implied cost of equity over CAPM. Take current price, build DCF with consensus
projections, solve for the discount rate that makes PV = price. This is more reliable
than beta-based estimates.

### Maximum Internally-Financed Growth
```
Max Growth = ROIC x (1 - Payout Ratio)
```

## Valuation Frameworks

### The Expectations Approach (Invert the DCF)
Instead of building a DCF to determine value, invert:
1. Take the current stock price as given
2. Reverse-engineer the growth rate, duration, and ROIC that justify the price
3. Assess whether those implied expectations are too high, too low, or about right
4. Invest when you believe actual results will exceed embedded expectations

This addresses every objection to DCFs: you're not setting inputs, you're reading what
the market assumes.

### MEROI (Market-Expected Return on Investment)
Translates a stock price into the implied return on incremental investment.
```
Steady-State Value = NOPAT(t+1) / WACC
PVGO = Enterprise Value - Steady-State Value
MEROI = Cost of capital x (Corporate Value / Steady-State Value)
```
If you believe the company can earn returns ABOVE MEROI, the stock is undervalued.
If returns will be BELOW MEROI, it's overvalued.

### The Commodity P/E
The baseline P/E for a company with NO value creation (ROIC = WACC):
```
Commodity P/E = 1 / Cost of Equity
```
At 8% cost of equity, commodity P/E = 12.5x. The market has historically traded ~35%
above the commodity P/E, reflecting that the average company creates some value.

### Warranted P/E Sensitivity (Growth vs ROIIC)
The relationship between growth and P/E is CONVEX, not linear:

| NOPAT Growth | Warranted P/E (at 20% ROIIC, 6.7% CoC) |
|---|---|
| 0% | ~15x |
| 5% | ~21x |
| 10% | 32.3x |
| 15% | 52.2x |
| 20% | ~100x |

At high growth rates, small changes in growth expectations cause ENORMOUS changes in
warranted P/E. A drop from 10% to 7% growth causes only 2.7% EPS decline but 22.9%
warranted P/E decline. This is NOT overreaction — it is math.

### EV/EBITDA: The Hidden Variable
EV/EBITDA has a hidden driver: the depreciation factor (EBITDA/EBIT ratio).
Higher depreciation factor = more capital-intensive = lower warranted multiple.
At identical growth, ROIC, and cost of capital, a company with depreciation factor 1.2
(capital-light) deserves a higher EV/EBITDA than one with factor 1.6 (capital-heavy).

### Four Quadrant Valuation Test
Plot companies on ROIC-WACC spread (x) vs expected growth (y):
- High spread + high growth: Highest multiples (~19.5x EV/EBITDA)
- High spread + low growth: ~14.0x
- Low spread + high growth: ~11.7x
- Low spread + low growth: ~11.4x

## Moat Assessment

### Five Sources of Competitive Advantage
1. **Supply-side economies of scale**: Fixed costs spread over units. Test: would 10%
   growth reduce average cost? If yes, below minimum efficient scale.
2. **Demand-side economies of scale (network effects)**: Value increases with users.
   Test: is it truly strong, or easily multi-homed?
3. **Switching costs**: Procedural (time/effort), financial (penalties), relational
   (emotional), and habit (underappreciated).
4. **Pricing power / intangible assets**: Brands (only if they increase willingness to
   pay), patents, regulatory licenses.
5. **Efficient scale**: Market only supports limited competitors profitably.

### Surplus Leader Margin (Hamilton Helmer)
```
SLM = [(Fixed Cost / Leader Sales) x (Leader Sales / Follower Sales)] - 1
```
If positive, the leader can price so the follower earns zero economic profit.

### Disruption Risk Checklist
1. Is the incumbent overshooting customer needs?
2. Is there a "not good enough" technology improving rapidly?
3. Is the entrant's business model fundamentally different?
4. Does the incumbent have asymmetric motivation to ignore the threat?
5. Is the industry shifting between vertical and horizontal integration?

### ROIC Persistence Base Rates
- ROICs are mean-reverting but persistent. ~25-35% of top-quintile companies maintain
  above-median ROIC after 10 years.
- Decay is rapid in years 1-3, then flattens.
- Differentiation strategies produce more persistent excess returns than cost leadership.
- Firm-specific factors explain 40-50% of profitability variance; industry only 10-20%.
- Market share alone is weakly correlated with profitability. Only market share backed
  by structural advantages (scale, network effects) matters.

## Capital Allocation

### The Eight Levers (Ranked by Typical Size)
**Investment:**
1. M&A (~4.3% of sales) — buyer returns negative on average (-1.6% announcement)
2. Investment SGA ex-R&D (~1.8% net) — the hidden intangible investment
3. Capital expenditures (~6.3%) — ~62% maintenance, ~38% growth
4. R&D (~3.3%) — ~75% investment, ~25% maintenance
5. Net working capital (~0.6%)

**Payout:**
6. Divestitures (~2.3%) — tend to be value-creating
7. Dividends — sticky, signal confidence
8. Buybacks — only create value when done below intrinsic value

### M&A Assessment (Sirower Framework)
```
SVAR (Cash) = Premium Paid / Market Cap of Buyer
SVAR (Stock) = Premium / (Buyer MCap + Seller MCap including Premium)
```
Base rates (1995-2018, n=1,267):
- 40% of deals greeted positively (avg +7.7%), 60% negatively (avg -7.8%)
- Of initially positive, 57% stayed positive after one year
- Of initially negative, 65% stayed negative after one year
- Positive deals had lower premiums (26.9%) vs negative (32.2%)

### Five Principles of Capital Allocation
1. **Zero-based**: Don't anchor to last year's budget
2. **Fund strategies, not projects**: A good project in a bad strategy should not be funded
3. **No capital rationing, but earn sufficient returns**: All capital has opportunity cost
4. **Zero tolerance for bad growth**: Exit value-destroying businesses
5. **Know the value of your assets**: Great allocators always know price vs value

### Intangible Investment Reality
Total US intangible investment (~$2.7T in 2024) now exceeds tangible capex (~$1.5T) by
roughly 2:1. Accounting still expenses most intangibles, making income statements
misleading and balance sheets incomplete. ~1/3 of buybacks merely offset SBC dilution.

## Company Life Cycle (Dickinson Framework)

### Cash Flow Pattern Classification

| Stage | Operating CF | Investing CF | Financing CF |
|---|---|---|---|
| Introduction | - | - | + |
| Growth | + | - | + |
| Maturity | + | - | - |
| Shake-Out | Mixed | Mixed | Mixed |
| Decline | - | + | Mixed |

Before classifying, adjust: (1) move SBC from operating to financing, (2) reclassify
intangible SGA from operating to investing, (3) remove marketable securities from investing.

### Transition Probabilities (3-Year)
- Growth companies: 44% stay growth, 38% move to maturity
- Maturity companies: 62% stay mature, 25% regress to growth
- Decline companies: 29% move to growth, 31% to maturity (recovery is common)

### TSR by Life Cycle Transition
Highest returns from companies transitioning INTO growth:
- Decline-to-Growth: +20% annualized
- Introduction-to-Growth: +19%
- Shake-Out-to-Growth: +15%
Worst: any transition ending in Decline (-17% to -3%)

### Valuation by Stage
Steady-state P/E baseline = 1 / cost of equity (at 9%, P/E = 11.1x)
~2/3 of stock market value comes from steady state, ~1/3 from growth expectations.

## Forecasting (BIN Model)

### Three Sources of Error
| Source | Nature | Contribution to Edge |
|---|---|---|
| **Bias** | Systematic (heuristics applied wrongly) | ~25% |
| **Information** | Incomplete data | ~25% |
| **Noise** | Random judgment variability | ~50% |

Noise is the most underappreciated and accounts for ~50% of the edge between
superforecasters and regular forecasters.

### Noise Index
```
Noise Index = |Estimate A - Estimate B| / Average(A, B)
```
Acceptable: ~10%. Real-world: 20-60%.

### Three Methods to Reduce Noise
1. **Combine judgments** (wisdom of crowds) — aggregate independent forecasts
2. **Use algorithms** — mechanical prediction consistently outperforms clinical judgment
3. **Mediating Assessments Protocol**: define criteria, score independently, then decide

### Four Methods to Reduce Bias
1. **Base rates (outside view)**: Select reference class, assess distribution, make
   inside-view forecast, decide how much to regress toward mean
2. **Premortems**: Imagine decision failed, write down why — generates 2x more scenarios
3. **Red teaming**: Assign individuals to argue the opposing view
4. **Signposts with probabilities**: Define milestones, assign numerical probabilities,
   track for calibration. Frequency of belief updating is the strongest single behavioral
   predictor of forecasting accuracy.

### Key Forecasting Insights
- Portfolio managers make good buy decisions but systematically poor sell decisions —
  selling a random position would produce returns 70bps higher per year
- Overprecision is the most important form of overconfidence for investors
- Distinguish strength of evidence (how extreme the signal) from weight of evidence
  (sample size). Overconfident when strength high + weight low.

## Second-Order Technology Investing

### Historical Pattern
The real money isn't in first-order enablers but second-order beneficiaries:
- 1900 Auto: Ford (1st order) vs Walmart (2nd order) — Walmart returned 1,622x
- 2000 Wi-Fi: Cisco (1st order) vs Netflix (2nd order) — Netflix returned 519x
- 2024 AI: GPU makers (1st order) vs automation users (2nd order)

### Value Stick Framework (Surplus Distribution)
How automation surplus gets distributed depends on life cycle stage:
- **Introduction**: surplus flows to customers (build share via lower prices)
- **Growth**: surplus flows to suppliers (consolidate supply chain)
- **Mature**: surplus retained by company (expand margins)

### AI Margin Impact Estimates
- Consumer Discretionary: +28% profit increase potential
- Information Technology: +17%
- Industrials: +12%

## Probabilities, Payoffs & Position Sizing

### Expected Value
```
Expected Value = Sum of (Probability_i x Payoff_i) for all scenarios
```
The Babe Ruth Effect: how often you are right matters far less than how much you make
when right vs how much you lose when wrong.

### Volatility Drag
```
Geometric Mean ~ Arithmetic Mean - (Variance / 2)
```
This is why volatility destroys compounding. S&P 500 example: 11.9% arithmetic - 1.5%
half-variance = ~10.4% geometric.

### Kelly Criterion
```
f = Edge / Odds
```
f = fraction of bankroll to bet. More attractive opportunities = larger positions.
Beyond Kelly-optimal, bigger bets lead to LESS return. Practitioners use half-Kelly.

### Ergodicity (Critical Concept)
Stock returns are non-ergodic (multiplicative). The ensemble average (many people playing
once) diverges from the time average (one person playing many times). A coin flip that
gains +50% or loses -40% has positive EV (+5%) but negative geometric return (0.95x
multiplier). You must maximize geometric returns, not arithmetic. This is why avoiding
catastrophic losses matters more than capturing big gains.

### Position Sizing: Confidence Assessment
Two opportunities with the same EV discount may warrant different sizes based on:
1. Reliability of available evidence
2. Range of reasonable opinion (would smart people disagree?)
3. Responsiveness to new information (would more study change the view?)

## Customer-Based Valuation

### Customer Lifetime Value (CLV)
```
CLV = M x r / (1 + d - r)
```
M = per-period margin, r = retention rate, d = discount rate.

CLV is extremely sensitive to retention:
| Retention | CLV (M=$100, d=10%) |
|---|---|
| 80% | $267 |
| 90% | $450 |
| 95% | $633 |

Moving from 90% to 95% retention increases CLV by 41%. Retention rate is arguably the
single most important metric for customer businesses.

### Customer-Based Corporate Valuation
```
Corporate Value = Sum over all cohorts of: [Number of customers x CLV per customer]
```
For each cohort track: acquisition rate + CAC, retention curve, revenue per customer,
contribution margin.

### Unit Economics Decision Rule
```
If CLV > CAC, acquire the customer.
CLV/CAC ratio of 3x+ is generally healthy.
```

### Dollar-Based Net Retention
```
DBNR = Revenue from prior-period customers this period / Revenue from those customers last period
```
Above 100% = expansion revenue exceeds churn. Company grows without new customers.

## Intangible Investment Adjustments (Detailed)

### The Problem
GAAP puts tangible investments on the balance sheet and intangible investments on the
income statement. This understates both earnings AND book value simultaneously. The
faster a company grows intangible spending, the larger the gap.

### SGA Decomposition
```
Total SGA = R&D + Advertising + Main SGA
Main SGA = Maintenance SGA + Investment SGA
```
Investment SGA has soared since the 1990s. Total intangible investment (~$2.7T) now
exceeds tangible capex (~$1.5T) by roughly 2:1 in the US.

### Industry-Level Investment Portions (Selected)
| Industry | Main SGA Investment % | R&D Investment % | SGA Life | R&D Life |
|---|---|---|---|---|
| Pharma | 68% | 89% | 4.2 yrs | 4.5 yrs |
| Computers | 66% | 80% | 3.3 yrs | 4.4 yrs |
| Retail | 38% | 91% | 2.4 yrs | 3.9 yrs |
| Avg | 54% | 76% | 3.3 yrs | 4.4 yrs |

### Impact
A pharma company's operating margin swings from -0.9% to 14.6% after adjustment.
S&P 500 aggregate: NI ~12% higher, book value ~49% higher after intangible capitalization.
This is why the traditional value factor (P/B) has weakened — P/B is systematically
inflated for intangible-heavy companies.

### High Gross Margin = Clue
Businesses with high gross margins are likely recording substantial investment within SGA.
If COGS is low, the real spending is in SGA — and that spending is often investment.

## TSR Decomposition

### Formula
```
TSR = Price Appreciation + [(1 + Price Appreciation) x Dividend Yield]
```

### TSR Driver Tree
```
TSR
  |-- EPS Growth
  |     |-- Net Income Growth (sales, margins, financing, tax)
  |     |-- Share Count Change (M&A, SBC, buybacks)
  |-- P/E Multiple Change
  |     |-- Steady-state P/E (1/cost of equity)
  |     |-- PVGO (ROIC-WACC spread x investment x CAP)
  |-- Dividend + Reinvestment
```

### Persistence Base Rates (Critical)
Net income growth correlation past-to-future is NEGATIVE:
- 1-year: -0.10
- 3-year: -0.20
- 5-year: -0.28
Extrapolating past NI growth is actively counterproductive.

ROIC: regresses toward mean over 5 years (35pp gap narrows to 15pp) but some companies
defy this — sustained ROIC above WACC IS competitive advantage.

### Value Trap Diagnostic
A stock that looks cheap but delivers poor TSR. Two culprits:
1. Below-average growth
2. P/E multiple contraction as PVGO deteriorates

### Buyback EPS Accretion Test
Buybacks are EPS-accretive only when earnings yield (E/P) exceeds after-tax cost of
funding. At 5% after-tax borrowing cost, only stocks with P/E under 20 benefit from
debt-funded buybacks.

## Growth Base Rates by Size and Industry

### 5-Year Median CAGR by Company Size
| Revenue | Median CAGR |
|---|---|
| $0-1B | 8.4% |
| $1-5B | 5.6% |
| $10-25B | 3.8% |
| $50-100B | 3.3% |
| >$100B | 2.9% |

### 5-Year Median CAGR by Industry
| Industry | Median CAGR | Std Dev |
|---|---|---|
| Healthcare | 10.4% | 30.6% |
| Technology | 7.9% | 16.5% |
| All | 6.5% | 16.4% |
| Manufacturing | 5.0% | 13.1% |

Intangible-intensive industries have BOTH higher growth AND higher dispersion.
Both tails are fatter — they can grow faster AND decline faster.