# Contributing

Thanks for being here. This project works differently from most awesome lists,
so please read this before opening anything — it will save you time.

## The one rule that explains everything

**Tools are never added directly.** Not by pull request, not by issue, not by
the maintainer.

Entries are discovered by scraping the `awesome-*` lists this project tracks,
deduplicated across them, then triaged with AI assistance and reviewed by a
human. The public *"Found in N active sources"* signal is the entire product: it
means independent lists mentioned the same tool, not that someone asked nicely.

Adding a tool by hand would take thirty seconds and quietly destroy the only
thing separating this from the hundreds of lists that merge any PR.

So: **pull requests that add tools will be closed.** It is not personal.

## How a tool actually gets here

1. **Discovery** — the radar scrapes the tracked `awesome-*` sources.
2. **Deduplication** — items pointing at the same normalized URL collapse into
   one entry, which is where the source-trace count comes from.
3. **AI triage** — a suggested verdict: GEM, WORTH_TRYING, MEH, HYPE or DEAD.
   These are inputs, never endorsements.
4. **Human review** — confirmed or overridden. Highlighted picks require a human
   GEM verdict plus a written reason.
5. **Labels** — entries surface as Human Pick, Worth Trying, AI Candidate,
   Popular Standard, Needs Review, Context Resource, Rejected or Graveyard.

Being listed upstream makes a tool **eligible to appear**. It does not
guarantee being featured, and it may land as Rejected with a stated reason.

Full detail is in [METHODOLOGY.md](METHODOLOGY.md), and the evidence behind
every trace is public in [data/latest.json](data/latest.json).

## Ways to contribute, most useful first

### 1. Nominate a source list

This is the highest-value contribution, and the one most needed.

Source coverage is the real bottleneck: the radar can only see what the tracked
lists contain. A good new source improves everything downstream; a single tool
suggestion does not.

Sources are judged on **freshness, activity, popularity, depth and community
health**. A list with thousands of stars and no commits in two years will be
declined — stale sources quietly poison the low-noise promise. That has already
happened to real nominations, so please check the last commit date first.

→ [Nominate a source](../../issues/new?template=nominate-source.yml)

### 2. Challenge a classification

Wrong domain, wrong label, a duplicate that should have collapsed, a verdict the
evidence does not support. These make the output measurably better.

→ [Open a classification challenge](../../issues/new?template=challenge-classification.yml)

### 3. Request human review

An entry sitting on an automated verdict that deserves a person looking at it.

→ [Request a review](../../issues/new?template=request-human-review.yml)

### 4. Suggest a tool

Least effective, but still welcome — it can reveal a gap in source coverage.
Expect the answer to be "get it listed upstream first" unless it exposes a
missing source.

If the tool is yours, **say so**. Disclosure is not disqualifying; hiding it is.

→ [Suggest a tool](../../issues/new?template=suggest-tool.yml)

## What happens after you open an issue

Issues are triaged in batches, not instantly. This is a small project — expect
days, not hours.

Issue state is meant to tell you **whose move it is**:

- `awaiting-upstream` — answered; the next step is getting listed upstream, and
  nothing is pending here. These get closed, which is not a rejection.
- `source-nomination` — a list being evaluated for the roster.
- `classification` / `review-request` — work queued on the maintainer's side.

If a tool lands in a tracked source and does not appear within a couple of
weekly runs, that is a bug here. Please reopen or ping.

## Conduct

Be straightforward and assume good faith. Self-promotion is fine when disclosed.
Undisclosed promotion, or pressure to add a tool outside the process, is not.
