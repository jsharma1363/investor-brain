# CS 153: Frontier Systems — Anjney Midha (Spring 2026, Lecture 2)

**Source:** https://www.youtube.com/watch?v=mZqh7emiz9Q
**Speaker:** Anjney Midha — Co-instructor, AMP Founder, founding investor in Anthropic/Mistral/Black Forest Labs
**Date:** Spring 2026
**Course:** Stanford CS 153: Frontier Systems

---

## Transcript

How many people have been to Coachella?
>> Oh my god. We got to do a field trip.
Mike,
>> I know.
>> Yeah. Okay. Maybe final project,
surprise project.
>> Go off.
>> Yeah. Yeah. Off-campus field trip.
So, uh usually when you have a um
uh when you go to a concert, for those
of you we will I will we will make sure
that you get to a concert, a real one.
Uh when you have a headliner, you need
an opening act, right, to warm up the
audience. And so, uh, today I'm your
opening act for the rest of this
quarter. We're going to have Mike, uh,
in the coming weeks as well, who's going
to be doing a deep dive into a bunch of
confidential computing stuff. But I'm
here to give you some context about the
speakers and the rest of the class. And
then we're going to do a bit of a deep
dive into the area of the world I
understand most, which is compute
infrastructure. Okay. But both today uh,
and for the rest of this quarter, these
really are your headliners. [snorts]
Yeah. Make sense? You recognize some of
these names?
>> All right. Woo. Yeah. For for um the
ones you don't recognize,
I I would recommend looking them up
because over the next few years, you're
going to hear about them a lot more.
Um
one extra thing we are considering
because many of you asked uh given the
just insane amount of demand we've had
both from speakers as well you guys to
add more topics and more coverage. We
might add a virtual um office hours
every Friday from noon to 2 pm
especially for speakers from who are
zooming in from around the world and
can't make it in person. That will be
optional extra credit. But quick show of
hands. How many people would actually
like that?
>> Oh, okay. I guess we got to do it, Mike.
>> All right, cool. More more details
coming.
>> More work.
>> More work.
This is the swag for this class.
Uh I forget who it was, but somebody
sent me a tweet. Apparently some there
was a tweet that went viral yesterday
about this class that said um be uh was
it be wary of taking classes that sound
like AI Coachella. Uh and there there's
lots more serious AI classes on campus
you can take. Totally agree. And by the
I I thought that was pretty fun. I think
AI Coachella is pretty fun. So as you
guys know, I did my undergrad here. uh
to grad school. And uh look, I I think
um we're gonna be talking a a lot about
technical stuff,
but we also get to talk in this class
about life and leadership. And so, um I
thought before we jump in to technical
stuff, you know, we talked a lot about
scaling laws last time and we're going
to talk a lot about that in this
quarter, but I thought I'll give you a
little less um sort of in preview into
Andre's uh life scaling laws.
Um,
you know, I I think that you should take
life seriously,
but not so seriously that you forget
what's important.
You know, don't forget how to have fun
and remember what makes life worth
living. Because look,
right now, you might feel like you have
uh all the time in the world, and
sometimes you don't know uh when you
don't have that much more time left. So
enjoy it while you can.
Don't take for granted.
It's a really magical time you guys are
in right now.
Um my view is it's very simple actually
to uh live life and scale yourself,
scale your impact which I know many of
you want to do.
Uh a lot of times a lot of you the
students we've taught over the last few
years have come to office hours and
asked an Mike you've been so successful
blah blah blah how do you plan your
future
um how you know it's very similar to how
do you plan a training run right you
want to you know really knock it out of
the park on capabilities you want to
scale capabilities and revenue like we
talked about last time and it's hard to
forecast these things so I I've actually
found a pretty simple heristic on how to
navigate
that journey which is just have fun
with people you enjoy hanging out with.
You know, that's pretty much it. I found
empirically, remember we talked about
how scaling laws are empirical, not
predictive. I found empirically
that's worked out pretty well.
So,
if there's one thing I'd love for you
all to take away from this this quarter,
you know, this is the last lecture I'm
going to be giving this quarter. We have
lots of speakers and so on.
Um, but this the I just want to leave
you with this one, which is
the most important people in this class
aren't really mi or the speakers. It's
you guys,
you know, look look around
and see uh how special it is.
You know, I um
Wow. Sorry, I I'm getting so emotional.
I need some water. Do you guys have Oh,
thank you.
Cool.
Really invest in these relationships
because you won't uh realize how they
come in and help you out in all kinds of
ways in in life. You know, as you guys
saw, uh I met my wife here as a
sophomore. Say hi, Viv.
We've been together 13 years.
>> Um,
and ju just uh as I mentioned I have
started two companies both with former
roommates from Stamford. Uh, one of them
is my current one AMP.
And you should just uh, you know, the
world is a
messy place. It's a can seem like it's
there's a lot of crazy stuff happening
in the world. We're fighting wars.
There's a lot of violence, a lot of
chaos. Uh but you guys in a very special
moment in time, you know, just think
about all the things that had to come
together for all of you to be sitting in
this room.
So just um
generally see how special and lucky you
are, you know, to be here.
And uh you know, we talked last time
about how it can feel. I think somebody
asked I I forget who it was who asked
the question an you know with all these
AI labs and big companies spending so
much on AI and infrastructure how could
we possibly create something interesting
or novel or new in science and
engineering uh and remember I said like
use them do things that don't scale or
be asymmetric about your bets and one of
those is you know obsess over the things
you love because uh that doesn't there's
some things that don't scale well
especially in large organizations and So
throughout this quarter, just remember
that you actually do have some special
weapons. And one of those is the uh the
obsessions, the love, the trust you have
for each other, the friendships, the
relationships you'll build here and over
the next few years because that'll come
in very handy and it'll be things th
those kinds of things are assets that
don't scale uh as as you join larger and
larger companies, organizations.
Okay, I'll stop being an uncle now. And
I will say maybe go to the real
Coachella while you still can. Uh, one
of my biggest regrets is uh when I was
on campus, we were working so hard and
staying so focused on on projects and
coursework. I I've never been to
Coachella, turns out. And so maybe we
we'll go with you guys. Okay. Shall we
shall we uh proceed?
>> Yes. Okay.
[applause]
Thank you guys. Quick recap.
Um
yeah, for those of you who are joining
us for the first time, I'm Anj. I'm one
of your co-instructors. There's Mike.
He's going to introduce himself during
his lecture as well.
>> Um my full name is pronounced an friends
called me an uh I was born in India. Uh
went to high school in Singapore, came
over for college here at Stanford many
years ago. Um and then I ended up
staying uh this is now my home. I live
in San Francisco with my wife uh in
Presidio Heights. And you guys are all
welcome to come by anytime you'd like.
I've been in love with applied machine
learning for the better part of of the
last 15 years. I came here as an
undergrad. I took a bunch of course work
in economics and a major that I don't
think exists anymore called mathematics
and computational science. And then for
grad school I did bioinformatics over at
the med school which is essentially
machine learning applied to healthcare.
Um I've always been a very applied
thinker. I've always found that it's
really exciting to look at what u
machine learning systems when taken out
into the real world at scale can tell
you about the world which is often
actually a pattern you see not just in
computer science but in physics right
physics is about trying to understand
how the world works looking at large
patterns empirically trying to figure
out are there laws we can derive about
the world um is this is the applied
physics uh part of of of uh the
discipline of course and uh I still
actually spend some of my time on campus
uh at the physics department as a
visiting scientist where we've been
doing a bunch of benchmarking on
frontier models and how they're good or
not at physics and science reasoning.
Feel free to ask me about that anytime.
We'll have office hours. Um over that
time I've had a chance over the last
1015 years to invest co-founder be part
of the early days of over 10 AI labs.
Some of those you guys know anthropic
mistral black forest. You'll be hearing
from many of these in this class. And um
as as we just talked about, I I'm I have
a deep deep uh I'm deeply thankful for
what Stanford has done for me.
Sometimes I uh [ __ ] post on Twitter.
Don't u um believe everything you read
on Twitter, but if you ever ever
wondering what my shower thoughts are,
that's where you can find me. My uh
handle is an MA.
Okay, this if you guys remember for
those of you who are here last time,
this is a cheat code to the rest of the
class and I think the rest of the uh the
next two years at least in the industry
outside of Stanford. Okay, this is not
just a CS153 thing. Hopefully, this will
give you a bit of a framework for how to
navigate life after college because if
you remember, we talked about the goal
of this class is preparedness for the
real world. The goal is not internships,
goal is preparedness. Okay. Um what is
happening
in the infrastructure world in the CS
systems world? We are going through a
massive change over the last 10-15 years
with the rise of um distributed systems
cloud infrastructure a some a somewhat
stable stack had emerged about how we
create ship and scale software right and
these are the different layers of the
stack that I would roughly say dominate
the industry. You start with capital
which is quite flexible. You can put
money in everything. Then you have land
power shell right energy production,
data centers, construction. On top of
that you or in the data centers you put
chips. You then have some software
infrastructure called a cloud that makes
those chips usable. And then you start
we hook up all these chips together. We
train a model. Sometimes we call them
agents. We then put them into an
application. We deploy them as
solutions. And then lastly um we try to
figure out how to actually govern these
things. What's the safety, the security,
the trust, the frameworks we need to
actually make sure that these these
technologies get deployed to the real
world. When Mike and I started this
class four years ago, it was called
security at scale. At the time, I was
running the platform or at Discord. How
many people have heard of Discord?
Perfect. Great. We did our jobs. U Mike
was running infrastructure at Apple at
the time. And both of us had started to
realize that security was becoming an
increasingly critical topic in the
world, but there just weren't that many
places for people like you guys to learn
what the frontier or the cutting edge
problems of security were because you
don't get to see those on campus. And so
this is this start this class started as
the missing systems class that I wish
had existed when I was an undergrad. And
so um that's where this all started.
Since then, it's evolved. We started
with 50 students. We're now 500. Thank
you all for for for joining us. I think
we have another 50 weight listed and a
few thousand people following al online.
I'm not sure when else we'll get to
teach this class again. So, let's try to
make the most of it. Yeah. Okay. We're
going through the great transition
because we have this new technology
called AI um that has unlocked
extraordinary value and is about to
unlock way more value. everybody at
every every leader or every major team
or or I would say um people who care
about the future at every layer of the
stack are wondering how do we unblock
the bottlenecks how do we make this
stuff go faster and safer and more
secure and what we're learning in the
industry as it is that it takes
revisiting a lot of basic assumptions
about how the stack works where in the
value chain you are what your job is
what your technical function is what
your economic function is and I think
you should start you will start to see
you all already are feeling what I'm
calling the great transition
um
to to uh driven by this this urgent need
across all levels of society right you
saw the sort of diversity in names we
have we have people like Jensen Huang um
and Lisa Sue at the chip layer coming in
to talk to you guys we have um folks
like uh Sacha Nadala who runs Microsoft
right who was at the cloud layer we have
Sam Alman how many people have heard of
Sam Sam Alman yeah There we go. Okay.
Um, he's coming by, right, to talk about
models and and how they're deploying
stuff. So, this is a really big shift
that's happening, right? For the first
time, at least in my life, I can't
remember a time when there was such a
big revisiting of assumptions up and
down the stack where everyone's trying
to figure something out. And that's
really cool
because that creates an extraordinary
amount of opportunity for you guys
because in times of uncertainty, that's
when things change.
and people who who understand where the
world is going, who have a point of
view, get to redesign the systems that
have stayed quite static in the past.
Okay,
I don't know what the new world is going
to look like. I don't think anybody
does. But for the next 10 weeks, you are
going to hear from some of the most um I
think uh dynamic, talented, and capable
leaders reasoning through how to really
unblock the bottlenecks at each part of
this ecosystem
every week. Cool. Sound good? Should we
keep going? Okay. No, you don't need to
clap for me every time. Don't worry.
[laughter] I got to let me let me let me
earn my my keep. Okay. So, quick recap.
Remember we we said what is going on at
the frontier,
right? The what is this this whole thing
about called intelligence?
And a few years ago uh when I was
starting to get calls from friends who
had gone to grad school with or who are
running research at places like OpenAI,
I started getting calls saying an you
know we think there's an opportunity to
really take some of this research out of
the lab and turn it into products and
services that could impact hundreds of
millions of people. And at the time it
was a pretty craft bespoke process,
right? And we talked last time about
pretty simple recipe on how to
manufacture intelligence compute data
algorithms pretty simple algorithm
transformer
do a little bit of pre-training some
fine-tuning good to go plug it into an
app you got chat GPT right we're going
to have Liam Fedis from chat the
co-creator of chat GPT uh come by and
talk to you guys later this quarter
things that look very different now
right in four short years we've taken
what was a pretty like I would say uh
bespoke process
and turned it into an industrial
engineering process at scale. Right?
Back then, 3 4 years ago, uh it the the
the sort of frequency of creating a new
model was maybe once a year, twice a
year. And today, we have this industrial
scale production process where we do,
you know, base model training at least
two times a year on 100,000 GB uh B300
equivalents. Um and then we do post
training with about 10% of that compute,
right? uh sorry mid-training we add more
capabilities into that and that happens
about two to four times a year with
about 10% of that compute and then we do
this thing called continuous post
training right with supervised
fine-tuning and RL and I won't bore you
with all the details that we talked
about last time we'll have assigned
readings slides will be up but I'll let
you guys go do the math uh on how much
compute and and and money is being spent
on these systems
um what's the most recent of course
development in all of this is that the
last mile of this the rein reinforcement
learning part is now consuming almost as
much compute as all of the rest of the
step pipeline combined.
Okay. And that's very exciting because
one it's new but it also means that
things are changing fast and resources
and strategies are consolidating and so
our hope over the next 10 weeks is that
you get a bit of a window a front a
front row seat into that part of the
ecosystem. Okay.
Okay. So what what does all this mean
actually for progress? This is where we
stopped last time and this is where I'm
going to pick off pick up today. A quick
disclosure list. Uh and sort of like any
good scientist. You you start by
disclosing uh the experiments you've
run, right? Uh this is a list of teams
that I've had a chance AI lab teams that
I've had a chance to work with. Many of
these were literally co-authors on a
paper that then we teamed up on to turn
into a company or project out in the
real world. Some of them I was involved
in as an angel investor, some as a
co-founder. And you'll hear from any of
these people over the rest of this
quarter. Um, but this is also a
disclosure list. I am biased. Naturally,
all my, you know, when you're when when
you're observing an empirical
experiment, you are naturally biased by
the data that you're fed, right? And so
between Mike and myself, what we've
tried to do is at least augment our
individual biases and work experiences
with a diverse sort of uh uh as
uncorrelated of a set of perspectives
for you all across the ecosystem as as
we could for in 10 short weeks. Okay.
Um so this is the crux of the class
right of of this lecture. What are the
bottlenecks on these capabilities?
Uh many of you are excited about these
capabilities. I certainly am. You know,
I, as we talked about last time, you can
use them for everything from
um, you know, having a conversation when
you're uh, by yourself doing your
homework. That use case is banned for
this one uh, for this class. Though, if
you do use any of the coding models for
your assignments, just tell us about
them. That's all fine. But it's a pretty
diverse sort of it's a pretty general
purpose technology, right? AI, these
foundation models.
Um, and so for the next, let's say 40
minutes or so, what I'm going to try to
do is is break down in detail at sort of
a systems level what is going on and
what in in in in terms of the the the
inputs required to keep these models and
these systems continuing their
blistering pace of progress so we can
all benefit. apply these this incredible
technology, you know, beyond chat bots
to neo areas like curing uh novel
diseases, discovering new materials, you
know, um I'm of the opinion that there's
just like there's an extraordinary
number of new frontiers to be explored
and developed uh with AI. Um but it it
would it's not going to happen without
us sort of as a society um figuring out
how to unblock progress in all the
domains that we care about. Okay, again
the recipe is pretty simple. I'm going
to break down the bottlenecks into four
major areas. Context, compute, capital,
and culture.
And we'll see how much we can reason
through this today. I'm going to start
with context and compute and then we'll
go from there. Okay, you might have to
do an extra overflow office hours or
something. Okay,
context.
Couple of pre prerexs you're going to
need to understand the next few slides.
reinforcement learning. Very simple
technique, super powerful, driving a ton
of the progress at the frontier today.
We talked about it last time. If you've
had a pet or you've had a sibling who
you've had to teach to stay away from
your room, you are a successful uh
frontier model trainer applying
reinforcement learning. The key idea is
that when you have a system that you
want to improve at a given set of tasks,
you don't tell the the agent or the
model how to do it. You just tell it
what you're what to do, what task you
want to reward, and when it completes
that successfully, you give it a reward.
If it doesn't do it successfully, you
withhold the reward and then you rinse
and repeat. Right? Very simple idea.
It's been around for a long time.
Started really working, I would say, in
earnest um at scale about two years ago.
And that was because when you initialize
a reinforcement learning environment
with an agent like an LLM that's smart
enough, has smart enough priors about
the real world, it turns out that these
systems learn much faster than usual and
and the capabilities tend to continue
scaling the more compute we throw at
them and the more um sort of
environmental harnesses and context we
give them, which is pretty novel, pretty
new. Earlier uh over the last 70 years
of computer science as we discussed
about the bitter lesson you know in
lecture one um RL would would plateau
pretty fast in different domains chess
right go etc. um it would it would sort
of surpass human performance but then
the rate of progress would sort of
plateau and the reason it seems again
this is I would say an open air of
debate is that the this the the the
priors the the previous sort of inbuilt
reasoning capabilities of of the the
models were just not general enough to
continue learning in a sense you know
after a while you guys know uh you've
heard the phrase you can't teach an old
dog new tricks uh whereas it turns out
you you can sometimes teach a Stanford
student to come back and teach new
classes. Right? This is my dad joke
kicking in as well. I I'll try to stay
away from from the puns. But so that's
this is the core philosophical tension
of RL, right? It's working much better
than expected. It seems to be because
LLMs have enabled a new era where the
the the models the language models are
smart enough to then give us new
capabilities when you use post training
to improve them on some specific task
benchmark or um capability.
It's making sense everybody following
me? No, I'm not see Okay, we're might we
might have to do an RL tutorial, but I
would encourage you to uh How many
people have taken a machine learning
class at Stanford already?
Okay, keep your hands up. How many of
you have at least uh done one pet set
with an RL problem?
Ah, okay. There's Okay, that's the
issue. All right, we're going to have to
about 30% or so.
>> We'll do an office hours on that. And
and you know, you're going to have some
of the co-inventors, some of the
pioneers around RL actually come talk to
you. So, uh they'll probably do a better
job than me.
But to recap, where does where does this
fit in to what's going on in the
industry? As we talked about last time,
you know, I got a call from some
friends, Dario and Tom, who were running
research at OpenAI four years ago. They
said, "An we want to leave and start a
new lab. Um, can we figure out how to
build a business around this?" And so we
spent some time fleshing out how do we
turn the scaling of capabilities into a
business, right? And this was the simple
recipe we came up with. raise some
money, buy some compute, augment it with
data, uh pre-train, put out a model
that's good enough, considered
state-of-the-art that some people like
programmers want to use them, deploy it,
do inference, you know, run the model
and that gives you two loops. The
inference hopefully gives you enough
money to buy your next round of compute
and gives you context feedback. You can
observe in the case of a pair programmer
when is the model actually accomplishing
the task you want it to or not. It has
your monor repo, your git uh history,
your uh local files, right? And then you
pipe that back that we call that context
the context feedback loop back through
RL hundreds and thousands of as many
times as you need with as much compute
as you need to improve the capabilities
of that of that system in that domain.
Pretty simple recipe, right? As I
discussed last time, we made 22
introductions uh I I I was an angel
investor at the time in Anthropic. Made
22 introductions to friends up and down
Sand Hill Road. They came back with 21
nos and a lot of them just said it
sounds sounds theoretically cool an as
an idea but do you have any empirical
proof? Do you have proof? Well, as you
guys know four years later we do have
proof. I won't bore you with all the
slides we talked about last time with
the um anthropic revenue etc. I think we
do have one slide later when we talk
about compute. So I'll come back to
that. Um
but it but to fast forward now I think
if you believe right that that recipe
works as you know anthropics gone from 9
to 20 billion in revenue Gemini is doing
well open AI's you know started to
produce extraordinary revenue there's
lots of proof that this recipe works the
question I keep getting over and over
again is okay well who wins who wins in
this that's going to if if everybody's
going to be applying this scaling recipe
on and it's so easy and repeatable then
where does the value acrew
And at least one opinion I I've started
to observe through all those empirical
experiments I talked about with you guys
earlier
is that context is critical here.
Context or the environment of the agent,
right? We talked if if you're training
your dog, it's to to fetch in a park.
That park is the context. It's the
environment. All the people in the park,
the kids that may be running around, the
grass, the physics of rain coming down.
All of those factors of the environment
influence the ability for you to improve
and train the system, your pet to
perform better and better in the real
world. Okay? And so I find myself
explaining this pretty frequently to
folks and I hope it'll make sense to you
is that one where will to answer the
question of where will frontier progress
uh continue most rapidly and this is
relevant for all of your projects
because many of you must be going okay
coding seems to be well on its way and
uh image generation is is also well on
its way. you we'll have um Andre Andreas
from Black Forest Labs who created
stable diffusion come by. But where else
can I make a difference? And one
question I would ask is well where is
there context right that can be reliably
measured and verified when you're
working with an agent and I think
wherever in life we have verifiability
you know code is very verifiable you can
write unit tests and your code passes or
not. um material science it turns out is
quite verifiable. Again, you hear from
you you will hear from Liam and Doge at
Periodic Labs about how they're using RL
from physical verification to discover
new superconductors. Very cool stuff.
There's a bunch of robots at a 30,000
foot facility in Menlo Park nearby that
maybe we do a field trip or something.
Um, but where else is the context and
the environment capable of verifying the
accuracy of the task as performed by the
agent? That's the question I would be
asking if I was you. The second question
that falls out from that is well, who's
going to capture that value, right?
Because you you don't want to just be
researchers. You guys actually want to
do sustainable frontier system
development, right? Not just one-off
model drops. You want to scale these
things. Okay. Well, it's the teams that
will have unique and defensible access
to some context. Do you get there first
or maybe you have some insight?
That's where teams will, I think,
capture the most value, right? So, that
those are the teams I think are going to
win. And then who's going to lose?
Um my view is that the teams that get
locked out of contexts that are
essential to improve these models and
the capabilities on some some domain
will not have a chance.
Now to bring that to life I thought I'd
just give you a few examples right of
this context these context loop wars
beginning.
Uh I think just about a year ago uh
there was a an
uh a news site a news um drop that
OpenAI
tried to acquire an IDE uh that many of
you probably use for your um for your
coding work called Windinsurf. How many
people have heard of Windsurf? Oh okay
cool I mean we'll be happy to hear about
that. Um, a few days later, right after
it was announced that Windinsurf was
being acquired by OpenAI, Anthropic shut
off model access to Windsurf users.
Doesn't happen often. You don't you
don't in in in our industry, we don't
usually shut off an API to users without
warning. But it made total sense, right?
Because if your competitor
needs access to your model the context
and can distill from observing how you
help out uh customers that you want to
attack that's leakage right you have
context leakage there and so to those of
us in the industry this was very clear
to me it was very normal I was not
surprised but I think for a lot of
people started updating their mental
model again remember that stack diagram
that if you're a model provider and then
you're an application company you can
always rely on your model company to
keep giving giving you intelligence.
Well, that was one assumption that that
stopped scaling then. Okay.
Um, and this is happening across the
economy in different contexts whether
it's consumers, creators, companies,
countries, and every part of the
economy. There's a battle that's raging
for these context feedback loops.
And over the next 10 weeks, you're going
to hear from many of these people. In
fact, you're going to hear opposing
views and uh that's our job here as
instructors. Our job is not to try to
convince you of our views. It's to try
and educate you uh with an independent
uh view as much as possible so you can
you know derive the conclusions you
believe about where the future is going
because look this is an open problem.
This is not a this again we're running
the grand experiment of how to keep
frontier progress going around the
world.
It's making sense. Yes. Okay, good.
People are nodding. Can I hear a yes?
>> Okay, thank you.
So, let's deep dive for a second. In one
of these, how many people have heard
about of Llama?
Great. One of the the creators of Llama
was a guy by the name of Guam Lump who
spoke in our class last year. His
lecture is up on YouTube. Go check it
out. Giam and his um college friend
Arthur who Arthur Mench who is going to
be speaking here a few weeks
teamed up a few years ago Arthur was a
researcher at deep mind he was um one of
the lead authors on a paper called
Chinchilla Chinchilla scaling laws have
been assigned as reading so I'm a good
professor never asks if students have
done the reading I'm going to assume you
guys have good faith honor code
definitely read that before um Arthur
shows up it'll tell you a lot about his
view but Mistral was a new Frontier Lab
started in Europe by the co-creators of
Llama and Chinchinilla and their view
was very simple. They said, "Hey,
there's going to be an extraordinary
amount of progress in closed source
models because that context is just not
that sensitive and people won't mind
piping their software engineering
context if you're a developer in Silicon
Valley to a cloud server somewhere. But
if it's a missionritical context, what
they call the sovereign context, it
matters to a government, it's national
records, defense, and so on. Well, you
kind of need to start locking that down
locally. And that means you need models
and weights that run locally on your
infrastructure that you can control. And
so they started Mistral as a way for um
companies, organizations that needed
control over their own context to deploy
models, open source models locally.
So that and and and and the reason I
think this is worth talking about is
because
it's quite um hard in the world of
infrastructure especially software
infrastructure to beat the the
relentless sort of uh flywheel of the
decreasing marginal cost of production
in storage in networking in servers. The
history of cloud over the last 15 years
has basically been decreasing marginal
costs, right? When Amazon and Google,
who both had sort of extraordinary
businesses serving consumers, right?
Google and search, Amazon and shopping,
they were just piling up lots and lots
of servers for their own needs and they
started realizing, hey, you know what?
It doesn't cost that much for us to add
another server and another server,
another server and basically just rent
that out to other people
because at some point the scale of your
own first party needs is so high that
you can pass on the benefits of that
scale to third parties. And that's how
we got AWS, GCP, Azure. Mike helped
start Azure. Sorry to date you, Mike. Um
but that's that you know basically 15
years of of sort of relentless uh
consolidation in the cloud
infrastructure world because of the
economies of scale right
for the first time in 15 years that's
changing
you know why do you have president
Macron the head of a country and Jensen
the world's richest man or was I think
last quarter probably still is um
showing up on stage in Paris uh next to
a 33-year-old scientist who's never run
a business before saying this is the
future of Europe
is because of context.
There are governments and mission
critical, you know, workloads that are
just too sensitive to be run on cloud
infrastructure overseas.
There's uh we talked last year um in the
class about the cloud act. How many
people have heard of the cloud act?
Okay, zero. H
We got a sign that is reading. The cloud
act is a um is policy that says that if
you're running workloads on United
States uh servers um whether it's or
it's a company run by um or it's servers
run by United States company globally
the government has the ability to access
that data
to some people around the world. That's
not okay. And so now suddenly AI
workloads have gone from being cool you
know chatbot assistants to being
missionritical systems. Remember we
talked about RL. RL has started to work
with a level of precision and accuracy
in mission critical context and that's
why you have a huge um sort of
reshuffleling of cloud infrastructure
globally and you'll start to hear this
word sovereign AI and infrastructure
independence a lot more over the next
few years. Okay. Uh just to wrap that
point, that's what's allowing startups
to sort of unbundle monopolies in the
infrastructure world or let me call them
igopies because some of our guests won't
be happy when I say monopolies um at
scale, at speed and scale. And this is
very exciting because you guys get to
participate in this revolution too. And
so, you know, one one clue you could
have about where to spend your time is
where there's a unique context that
hasn't been available to you because
you're not at scale, but that you can do
something unique and get ahead of and
start um sort of being a participant in
that restructuring of of that industry.
Okay, make sense? Yes.
>> Come on, guys. It's spring.
>> Yes. Okay. Thank you.
Okay. So, how do you actually get this
going after doing this for 10 years and
mostly five of intense uh investing
company co-founding? Nowadays, people
call me the founding investor. Basically
means I'm neither the uh the the the
CEO, which is all the many of the
talented folks I get to work with who
are usually scientists, but I'm not sort
of a traditional venture capitalist. I
don't really write a check. I typically
co-ound these companies on day one with
these teams. And I do this one at a
time. My current um project is Periodic
Labs, as we've talked about.
But I've observed a pattern over and
over again which is you you you you you
sort of formulate a state-of-the-art
mission. What is a frontier that we
really want to advance material science,
coding, whatever it might be and that
you make that your mission. We want to
move the frontier. We want to create
state-of-the-art intelligence in a
particular domain. Okay. You then get
enough compute. That's research compute.
You do some experiments. to figure out
how can we actually get something novel
out to the world that doesn't exist. And
often in a new domain, that's it's
actually not that hard to do because
we're early,
ship it, get it out into a context that
you have access to, run the feedback
loop, and then remember we talked about
that scaling the those two flywheels.
Then just keep them going. Keep them
going as long as you can because that is
the gift that keeps giving because they
reinforce each other. Okay.
Eventually, at some point, when these
flywheels get good enough, they start
propelling themselves. That's what many
people in the industry call recursive
self-improvement. Sometimes people like
to call this the path to AGI or ASI. Um,
well, I'm an infrastructure guy, so I I
think more at the level of the system. I
don't necessarily think in terms of a
model, but you can often have a company
that's, you know, hitting takeoff
because they've just figured out as a
good execution team on how to keep
recursively improving themselves. It
doesn't have to be an actual model
that's super intelligent or whatever. I
mean, that's that's one view. That's
fine. You guys should ask our speakers
if that's how they imple they they view
it. But I I sort of think about
recursive self-improvement at the
systems level that's that's attacking
the state-of-the-art mission not really
at an individual model or API level.
Okay. Um so the big question where does
this leave us right on the context
question is what are the limits to RL?
Um and this is a very exciting open
question. I don't I hope this will be
answered um over my lifetime. It may not
be. I don't know how much time we have
to really figure this out. But there's
two views on it today that I hear in the
industry. One is a philosophical, the
other is the the empirical view. The
philosophical view is that hey, given
the right context, given sufficient
compute,
these agents should be able to learn
anything. So once you get that r like
recursive sort of takeoff happening, why
don't you just ask the agent to constru
if it you have a coding agent, right?
and the coding agent is not very good at
material science, but at some point if
it's good enough, you just tell the
coding agent, please build yourself a
material science environment and then go
do the RL loop yourself and so on and so
forth. That's one view.
Um, it's not clear right now to me that
RL is generalizing outside of task
distributions, which means outside of
the domain that you started that
frontier flywheel in, right, the context
feedback, it's now clear to me that
models are generalizing from, let's say,
coding to material science to biology,
etc. I think within the narrow
distribution of coding and so on, what
we're seeing is basically relentless
progress. It doesn't look like it's
stopping anytime soon. And look, this is
a big area of debate, billions of
dollars being invested in trying to
figure the answer to this question. My
view is closer to the second one, which
is that empirically what I've observed
is that life is messy.
Um,
progress is fastest and easily
verifiable domains. And so in domains
like coding, which is verifiable, you
will start to see sort of the idea of a
narrow super intelligence or, you know,
exponential progress. But in areas uh in
the world where progress is not as
easily verifiable and a great example of
that is aesthetics,
beauty, love like h how what are these
the how how do you verify right like
what is good a good a good verifiable
construct for beauty or love or
aesthetics and this is why how many of
you have tried writing a uh like a
message to your like an extended blog
post or something with with Claude or
Chad GPT
only four or five people. Okay, clearly
you guys have real work to do unlike me
writing blogs all the time. Um, it's
terrible. These models are not good at
long form writing at creative writing.
They hallucinate. They they make these
cliche hyphens and so on, right? They
you see the m dashes and the it's not it
this this is a game changer. Ever ever
heard of that phrase or the it's not
just X,
it's Y?
I I sent a a blog post. I was writing
like a bit of a manifesto about
infrastructure to a friend three weeks
ago who's a founder you'll hear from in
this class. Said, "Can I get your sanity
check on it?" He writes back in 30
seconds, "Did you use Claude for this?"
I was like, "No." He's like, "I don't
believe you." Well, it turns I had
written the outline myself and then I'd
asked Claude to like flesh it out. You
know, we've all done it, right? And he
could tell immediately. And since then,
we have an internal rule at AMP. We
don't send each other AI generated uh
documents. We think, we sit, we write,
and we share with each other even if
it's uh raw.
So many of the speakers you're going to
hear from at, you know, working in the
model level are innovating here, trying
to answer this question. And I'd
encourage you to do some research on
them. A lot of people share openly about
their strategies online. So, so do your
homework, come prepared, push them on
these questions. Yeah, the more you prep
you do, the more work uh the more value
you're going to get out of these
lectures. And more importantly, I think
you guys
can innovate here too because it's early
and there's so many domains that maybe
you only you understand and only you can
verify because of your obsession, your
love, your taste, your sense of beauty,
your your culture. And I think we're
that I think that's the most uh valuable
thing you could be doing when I when I
get a call from a new team that wants me
to invest or help them build a business.
That's what I'm often looking for is
what is the unique
um sort of frontier that they can verify
for humanity. I had one of my uh
favorite he's he might not like me
sharing this but I'll share it anyway
and we we'll publish after getting his
um permission. How many people here have
heard of the YouTube channel three blue
one brown? Whoa. Okay. I did not realize
I'm gonna have to call Grant. Uh Grant
Sanderson, who is the uh the creator of
three one three blue, one brown,
and I were uh undergrad draw mates. He
lived in Froso. I lived in Ooj. Uh there
were four of us who were good friends.
And then we drew into Kthers together.
Yeah, Kthers. Uh but uh Grant and I have
stayed in touch over the years and he
came by. He crashed over at my house for
the last two days and um he
unfortunately had to fly out this
morning at 6 a.m. We, you know, were
talking late into the night last night
about what would it take to create um
sort of a a truly world-class
educational um you know, learning space
of the kind three blue one brown does
for science and math, but for anything,
you know, and it was so clear to me
while talking to him that that what's
unique is is his brilliance of how and
his taste for what is is the right way
to deconstruct a really technical topic
and really understand it from a from
first principles and that's I would say
the true magic of of frontier research
is is is distilling the insight of
somebody who's really world class at
what they do and being able to share
that with the world and RL is just one
technique to get there I think we'll
invent many other techniques okay making
sense
>> oh my god guys
>> yes thank you okay now compute this this
is the exciting stuff for me. I'm a
computer nerd. I'm an infrastructure
nerd. As you know guys, as I talked
about earlier, I studied both economics
and computer science and statistics and
bioinformatics. And I love the
intersection of multiple domains and
compute and infrastructure is really
where a lot of that comes together. How
how long do we have? Quick time check.
>> 30 minutes. Okay. Where's Anthony?
Hony's last year. Dice, can you keep me
honest and give me a heads up when we
have 10 minutes left? Okay. Thank you.
So what is the big idea with scaling?
It's that scaling works predictably,
right? Capabilities scale predictably
with compute.
This is a uh set of public estimates
that overlay anthropics revenue over the
last four years correlated with the
amount of compute that they brought up
at the company. What do you notice?
Anything? Anyone notice something about
the shape of the curve?
exponential
every time.
You know, I wouldn't even go I wouldn't
go that far. I wouldn't say it's
exponential. Actually, it it is it is
correlated strongly with the compute,
right? Um it's predictable. Every time
the company brought up new compute,
roughly 60 or 90 days later, there was a
capabilities jump and then a revenue
jump.
That is quite special.
Dollar in, dollar out.
Dollar of compute in, dollar of hard
assets, land, power, shell, which in the
financial markets usually trade at three
to four times revenue
being turned into a dollar of software
revenue, which usually trades at 30 to
40 times revenue. From a systems
perspective, what's going on?
We have developed a predictable way to
transform
one input
into another predictably that humanity
considers a lot more valuable than the
input. The output here is roughly 10
times more valuable to the world to the
markets than the input. Remember this
class is called frontier systems. We
stopped calling it security at scale and
infrastructure at scale for a reason
because we are now in the full stack
rewrite. And I need you guys to start
thinking up and down the stack. Not just
as engineers, not just as or computer
scientists or electrical engineers. I
need you to start thinking like full
stack thinkers. Think about the the
capital markets. Think about the
business because if you want to keep
sustainably doing research at the
frontier, you've got to run the whole
loop. Run it back. Okay. So,
what's an example of that in production?
If you look under the hood, cloud code,
this these are commits that uh the agent
has been making publicly on GitHub
beautifully correlated with the compute
buildout, right? So this is not just
revenue. Somebody asked I think last
time an is just like revenue pumping
this is real usage.
Sure, over here there's probably some
verbose cloud uh
you know commits, overeager commits, but
by and large this trend has been pretty
reliable over the last four years. And
so even if you took revenue out and you
just looked at usage, right? This is
very real fast growing exponential usage
in coding.
For this reason,
the great trans what what I've called
the great transition in infrastructure
started last year. Once this this
predictable scaling not just of
capabilities but of revenue of this
infrastructure trade became legible to
the capital markets.
Everything changed
right
over the last three years.
The five largest tech companies have
decided to spend more on infrastructure,
land, power, shell, than they have in
the preceding 30 years combined.
Last year, they're going to they they I
think spent 300 billion. This year
they're going to spend 600 billion. Next
year they've announced in their earnings
reports they're going to spend $1.2
trillion on capex. These numbers are
kind of hard to fathom.
So,
what happens? What happens when all the
big boys start spending? What do you do?
Step one, acknowledge reality.
For the last four years, I have I have
lost the count of the number of times
people have called me and said, "An why
are you spending all this time on
compute? It's a commodity.
Just give the company some money.
They're going to go be able to rent from
GCP, AWS, and so on. It'll be that's how
the world works, right?" Not quite.
This is a chart that we've been
aggregating at AMP of uh rental GPU
rental prices quarter by quarter across
a number of estimates. We have an
internal system we call the AMP grid
whose job it is to try and understand
what's going on in infrastructure and
try to forecast intelligently so that
our teams and our companies that we work
with can get a bit of a empirical view
on where infrastructure is going.
What do you observe about the price
trend of H100 prices? a chip that's over
two years old
over the last 90 days.
Somebody come on this. Yes. Thank you.
Going up.
It's pretty simple.
Anybody who's told you chips are a
commodity
should probably get a phone call from
you and ask them what they think about
this because chip prices are not going
down, they're going up.
Two years ago when I was calling friends
of clouds up and trying to rent them for
our teams and I was the the the average
H100 price per hour was a $1.73
this morning. Where's Sebastian?
Sebastian here. We got a friend message
and say, "Oh, hi Amy." Can we give a
quick round of applause for Sebastian?
Amy,
[applause]
the reason I'm doing that is cuz you're
going to be thanking him later.
Sebastian is your chief comput intern
for this class for your final projects.
When you need compute credits, he's
going to be provisioning them for you.
And so, if you have any bugs and so on,
please don't come to me. Go to Seb. Seb
and Amy, who are also married and I
think uh and met at Stanford here, been
married longer than Viv and me um were
our undergrad friends. And uh Seb was my
master of rituals in AKsai, which I uh
pledged mostly to be able to date Viv.
Okay. Um
and Seb Seb is my co-founder at AMP, so
you can bother him anytime you want.
Okay. This morning we had a founder
who's raised I think like what $700
million billion dollars. I wish I could
show you the screenshot. Said, "An we're
in a compute crunch." Yes.
Need H100s ASAP?
How many do you need and when?
Take them right now.
Price not a problem.
It's a good time to be a drug dealer.
Right?
This is a fundamental assumption the
entire industry has been built on that
chips are a commodity. Old chips
depreciate. Entire publicly traded
companies are running on this
assumption. Meanwhile, here ground zero
in Silicon Valley, I can tell you it's a
very very different picture that's
emerging.
Okay. So, where what does that mean?
I like to look at history to get clues
about where the world is going to go.
And I'm starting to realize that we've
seen this before.
We've lived through cycle after cycle of
the invention of new infrastructure,
general purpose technologies,
and then you invent ways to turn that
technology into useful products, steam
engine, right? Make cars, make shoes,
whatever it might be. And that results
in what is often called the golden age
or the guilded age where few people who
start hoarding those resources
get to profit at scales we've never seen
before.
And I think that's roughly where we are
relative to the industrial revolution.
So what happens next, right?
Like I said, let's look at the history
of infrastructure for some clues. This
is the econ nerd in me coming out, but I
promise we'll bring it back to computer
science.
I just thought I'd pull some I asked our
friend Claude to pull some charts
together. So if there's some uh wrong
numbers here, I'm not to blame. Though I
guess I'm not following my own rules
here.
But with steel 1867 to 1895, right?
There was, if you notice, this increase
in prices.
Then there was this panic of 1873
where there was a lot of hoarding of the
steel and prices were going up. Then
suddenly there was a panic. Oh, this
steel actually isn't worth very much. We
we hoarded too much steel. Suddenly the
prices collapse.
Super annoying for everybody involved.
Companies go down. people are
backstabbing each other. Markets are up
and down. Wars are being fought. Blah
blah blah. Eventually, as a society, we
get together and say, "Okay, this isn't
good. We don't want panics. We want
stable production of steel, stable
consumption of steel. Let's figure this
out."
And that's what you what results in this
sort of plateauing of uh of steel.
Same with fiber optics. I'm sure
everybody here is tired of hearing the
word AI bubble. Um, everybody's asking
about the fiber optic overbuild and all
these companies like Cisco, Lucent,
Nortell, Worldcom. Is this, you know,
are these chip companies the same? Why?
Because all the economists, all the
people writing opeds in the Wall Street
Journal are just looking at all the same
data. Okay, prices go up and they come
down. It's a bubble boom bus blah blah
blah, right?
Same thing with DRAM. Very violent
semiconductor cycles.
Memory was invented. DRAM was invented.
people go, "Okay, this is really
important for personal computing."
People start hoarding it. Then there's
uh some something happens. Usually, it's
a panic. It's some It's usually,
honestly, it's not something not that
big. It's like some some stupid news or
some world event. There's always world
events happening, but triggers a panic
and that results in a self-fulfilling
sort of selloff of infrastructure,
stocks, assets, supplies,
and then you get back up and people
realize, no, actually this there's
inherent valuable technology with this.
There's new capabilities here. We can do
something with it. And then you either
get another rise or you have a
stabilization of that resource.
This is the Baltic dry index with
shipping. Same thing. These slides will
be up. I'm not going to bore you with
it. Uranium.
When we were living through the nuclear
energy boom of the 1970s,
same thing,
right? And often what happens and with
uranium this is very clear. you have an
uh uh the intervention of the government
to allow the stabilization of that
resource. And so if you look over and
over again and okay and this is our our
friend the H100 GPU that we talked about
prices were dropping after the chip came
out in June all the way till August of
2024 and since then they've steadily
been rising. This is actually a bit out
of date but as you know they're back up
right. So what does history tell us? one
infrastructure does is cyclical.
So at least we've got some clues
hopefully unless this time is so
different which it may be and which is
what I should I would encourage you to
to quiz our speakers about because many
of them are at the frontier of these
markets.
Hopefully we as a society can figure out
how may ideally we just skip the whole
boom and bust thing. It's not fun for
anybody.
But assuming that's we're we're at the
start of another sort of like panic run
on compute, the question of course,
right, is how do you stably get to the
other side as fast as possible so we can
all start building useful frontier labs
and projects without having to go wait
at the around the corner and and bother
Larry and Sergey for compute.
[clears throat]
Now the usual timeline if you just look
across the digital era you know the
internet and uh bandwidth buildouts
between these cycles is about 3 years
2.8 8 years for physical infrastructure
it was 6.3 years
and my best guess well and this is the
thing about AI that's so novel it's a
combination AI scaling is a combination
of massive you have to marshall massive
physical resources right like land power
shell um chips
to produce this very digital thing
called software revenue intelligence is
is is is bits but but the production is
atoms Those
worlds don't like colliding
and that's what's new here and
scrambling and confusing a lot of people
is how do we actually coordinate these
two things in a way that's sta stable
reliable and so on.
The central question of course right is
how do we get compute or is compute
rather just a commodity right that those
are that's the tension we've been
talking about over the last 15 minutes
is compute a scarcity
is it something where all of you should
be spending your time wondering should
you be making chips
should you be making more and better
interconnect or should you be spending
time on distilling your aesthetics your
creativity your intelligence like three
blue, one brown into how to teach the
world new kinds of science and math and
physics. That's the core tension, right?
Good news is this class covers both. So
for those of you who are electrical
engineers and want to go into chips,
you're getting that uh exposure. And for
those of you who want to be frontier
model researchers, you're going to get
that exposure. You can decide, okay?
We're not here to decide for you.
But here's my view on it as one
participant. macro I today unlike
electricity or coal computable
electricity is fungeible right megawatts
or megawatts or megawatts everywhere you
pipe into a grid you get them out
it wasn't always the case and I'm going
to talk about that in a sec but today
compute is not a commodity the prices
are rising and they're not fungeible
this chart shows that there's varying
prices for different chips let forget
chips from different companies like AMD
and Nvidia. Chips from the same
manufacturer are not funible, right? The
H100 is different from the GB200 which
is different from the B300. These
numbers may not mean anything to you.
This is what I spend all day talking
about with my research teams. So number
one, the problem or the indicator that
compute is not a commodity is that
compute is not funible today. And two,
forecasting compute at the micro level
is very very hard. Unlike electricity
where we've developed pretty stable
mechanisms for how to forecast our
consumption, barring hurricanes and so
on, there we're generally like we have
power here, right? I grew up in rural
India in a boarding school called Rishi
Valley and we used to have power outages
roughly once in the summer like every
other week. today. Luckily, I think
they've put a transmission like a uh
they built a generator backup generator
there. But in the in in most parts of
the world, we've had stable forecasting
of energy and therefore the stable
production of that energy and supply for
what at least 75 years.
That's not the case with compute because
inside of these research labs, one team
finds it very hard to reason about their
needs. Training is a is a is a spiky
thing. You think about okay how do I
create a new capability like a frontier
model for coding you take an algorithm
you play with it on sort of small scale
if it starts working then you spike up
for your hero training runs inference
when you deploy your chatbot turns out a
lot of people you especially if your
chatbot's deployed in the US a lot of
people use it during the day no one's
using it at night inference is cyclical
too and so we're in that part of the of
humanity where um Not only is the most
valuable input to production of
intelligence not funible, it's also
super hard to forecast.
And as a result,
um, we have those hoarding cycles going
on. Remember I showed you those, uh,
sort of the big boys buying up as much
land power shell as they can over the
next four years going, look, there's a
pretty reliable trade we can make,
right, for hardware to software revenue.
Not sure which research, which model,
which breakthrough will actually do
that, but we might as well just buy it
all up.
So the question I spent a lot of time
recently thinking about and I think you
guys should for those of you who are
interested in infrastructure is what
what did it take in history
to turn this scarce monopolized
production resource into uh a productive
sort of accessible commodity for
everyone who's working or innovating in
the field.
Okay. And my view is again history tells
us that there's two key things you need
to solve the funggeability and the the
the access problem. One, you need
standards
AC/DC,
right? TCP IP, these standards that we
convene on over and over again to say,
you know what, this is infrastructure.
It should be stable. Let's all agree on
a standard, a format for this
infrastructure to be produced and so we
can all consume it no matter where it
is. And the second is you need
institutions to enforce those standards
because inevitably humans are misaligned
at some scale.
And somebody needs to coordinate and
align human beings to adopt those
standards at scale. And that's roughly
where we are right now. So what makes a
commodity fungeible? It's pretty simple.
Commodity needs a This is all How many
people have taken econ 1A?
Oh wow. Okay. We got to do some econ
assignments too for those of you who
want to work at the frontier. This is a
pretty standard textbook definition of a
of of funability. What makes a commodity
fungeible? A commodity needs a common
unit. It needs a standard delivery
interface. It needs interconnection and
pooling. Needs metering, control, and
settlement. And the buyers can
substitute one supplier's unit for
another.
Okay, you should uh really understand
this definition if you intend to train
any kind of frontier models because this
is not the case today.
So this was my point. Technical
standards and fungeibility don't come
easy. They need institutions to enforce
them to reallocate away power from those
who benefit from hoarding and instead
prioritize the public benefit.
That's what we need more and more of in
these infrastructure cycles is somebody
or some group of people need to start
stepping in and saying, you know what,
good for you. Great. You have enough
compute.
Those folks over there don't. Let's pull
and let's figure out an optimal
allocation of this resource across
society, across a country, across the
world. That's what we um called the
public benefit.
>> Yep.
>> 10 minutes. Okay, perfect. I will try to
zip through this. We're almost at the
end.
So, the punch line is pretty simple. We
are in the pre-standardization
of compute era, right? If you just look
at all the previous cycles, railroads
from 1886, electrification 907,
telephoneony, aviation, internet,
semiconductors,
new new general purpose technology,
huge explosion in infrastructure needs,
usually consolidation amongst three or
four players.
Hope sometimes industries step in and
self-regulate and they come up with
standards if they can get along. Other
times they a government an institution
has to come in and say these are the
standards and we're at that moment
roughly in history for for compute.
So food for thought for this quarter.
This is your assignment and there'll be
some readings but I'd like you to keep
this at the back of your minds. One,
what will it take to ensure a peaceful
transition on compute over the next
couple years?
[clears throat] And two,
what is your part in this? You can be a
part of this change because remember I
said at the start of this lecture,
you are extraordinarily lucky to be
alive at this moment in time. It may not
be clear to you and it's always uh you
know it's easier to connect the dots in
hindsight, but think of yourselves not
just as students but as active
participants. And part of the goal and
design of the um the project this
quarter is to try to make you more and
more active participants in this stack.
You can blog, you can tweet, you can
write, you can share your thoughts with
the world on what are the standards you
wish you know you emerged so that your
job could be easier and hopefully
>> [clears throat]
>> um some of the people in this room who
are going to come talk to you who are
running many of these institutions who
can can help evangelize these standard
standards adopt them coordinate them
will hear from you.
Cool.
All right, that's all I've got. Um I
have a bonus. This is from last year.
This is a screenshot of RTX 5090 prices
in USD over the last 18 months. Who
knows what the RTX 590 is? Okay, cool.
Some gamers in the audience. This is
Nvidia's gaming chip.
It was also the grand prize for the best
project last year when Jensen came by.
He signed 55090s. I think uh this is
Abel whose team made a really cool
gaming
uh
product and and and
pretty valuable chip, right?
So, I'm not going to ask Jensen this
time for for more 590s because they're
they're a little bit more valuable this
time around, but we'll see. Maybe it'll
be surprises. Okay, thank you guys.
