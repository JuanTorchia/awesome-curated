# Awesome Curated Methodology

Awesome Curated is a weekly audited radar of developer tools discovered from active `awesome-*` repositories. The goal is not to mirror every list on GitHub; it is to produce a lower-noise shortlist with source traces, deduplication, AI assistance, and human review.

## Sources

The input layer tracks upstream `awesome-*` repositories as sources. Sources can be active roster entries, bench candidates, rejected entries, or inactive entries. Public counts focus on active roster and bench sources.

- Active sources in current snapshot: 20
- Raw items scraped: 38659
- Curated entries at current threshold: 1182
- Approximate duplicate/raw noise removed: 37477

## Discovery and Scoring

Discovery uses GitHub repository metadata and README parsing. Source quality is informed by freshness, activity, popularity, depth, and community health. These signals help choose which upstream awesome lists are worth tracking, but they are not a guarantee that every item is good.

## Deduplication

Items repeated across sources are grouped into one curated entry when they point to the same normalized URL. The public signal "Found in N active sources" means the tool appeared independently across tracked upstream lists after deduplication.

### Cross-source threshold

An entry becomes publicly visible only when at least 2 independent tracked sources list it. Entries found in a single source stay in the internal queue: they do not appear in this README, in [TOOLS.md](TOOLS.md), or in [data/latest.json](data/latest.json), no matter how popular, well-maintained, or widely adopted the tool is. Popularity is never a reason to include an entry, and never a reason to exclude one — only independent source consensus is.

This threshold is the main noise filter, and it is what makes the radar a consensus signal rather than a mirror of any single upstream list.

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

The cross-source threshold has a known blind spot. Coverage is bounded by which upstream lists are tracked, so an excellent but ecosystem-specific tool can be listed by only one tracked source and stay invisible here. Where a single tracked list covers an entire ecosystem, no tool unique to that ecosystem can reach the threshold at all. When a well-known tool is missing, this is the usual reason — not a classification error.

## Latest Generation

Generated on 2026-08-01 from the juanchi.dev Awesome Curated pipeline. Evidence snapshot: [data/latest.json](data/latest.json).
