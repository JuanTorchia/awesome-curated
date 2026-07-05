# Awesome Curated Methodology

Awesome Curated is a weekly audited radar of developer tools discovered from active `awesome-*` repositories. The goal is not to mirror every list on GitHub; it is to produce a lower-noise shortlist with source traces, deduplication, AI assistance, and human review.

## Sources

The input layer tracks upstream `awesome-*` repositories as sources. Sources can be active roster entries, bench candidates, rejected entries, or inactive entries. Public counts focus on active roster and bench sources.

- Active sources in current snapshot: 20
- Raw items scraped: 33416
- Curated entries at current threshold: 1182
- Approximate duplicate/raw noise removed: 32234

## Discovery and Scoring

Discovery uses GitHub repository metadata and README parsing. Source quality is informed by freshness, activity, popularity, depth, and community health. These signals help choose which upstream awesome lists are worth tracking, but they are not a guarantee that every item is good.

## Deduplication

Items repeated across sources are grouped into one curated entry when they point to the same normalized URL. The public signal "Found in N active sources" means the tool appeared independently across tracked upstream lists after deduplication.

## AI Assistance

AI classification helps summarize and triage entries into suggested verdicts such as GEM, WORTH_TRYING, MEH, HYPE, or DEAD. AI suggestions are inputs for review, not final endorsements.

## Human Review

Human-reviewed entries are tools where Juan has confirmed or overridden the automated suggestion. Highlighted picks require a human GEM verdict and a visible reason for inclusion.

## Source Traces

Staff Picks expose the upstream sources that mentioned the tool. A trace includes the source repository, source status, source quality, upstream item name, and observation date when available. The public evidence snapshot in [data/latest.json](data/latest.json) is the inspectable source for these traces.

## Public Labels

Public labels are reader-facing and separate endorsement strength: Human Pick, Worth Trying, AI Candidate, Popular Standard, Needs Review, Context Resource, Rejected, and Graveyard. AI Candidate means automated triage suggested promise, not that Juan endorsed the tool.

## Caveats

Every Staff Pick includes a short caveat. Caveats call out scope, maintenance, popularity, security sensitivity, or adoption fit so the top section does not overstate certainty.

## Inclusion Rules

Primary tool recommendations should be developer tools, libraries, frameworks, platforms, or tool-like projects with a clear use case. Stronger entries have independent source consensus, useful descriptions, active upstream signals when available, and a defensible rationale.

## Exclusion Rules

Top recommendations avoid tutorials, videos, playlists, pure learning resources, generic homepages, duplicates, abandoned projects, and entries without a clear reason to include them. Learning resources may still exist in secondary domain pages when useful, but they are not primary Staff Picks.

## Limitations

Classification can be imperfect because upstream awesome lists mix tools, articles, videos, companies, and broad platforms. GitHub metadata can lag or be unavailable. If something is misclassified or missing, open an issue with the link and reasoning.

## Latest Generation

Generated on 2026-07-04 from the juanchi.dev Awesome Curated pipeline. Evidence snapshot: [data/latest.json](data/latest.json).
