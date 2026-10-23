# Research retrieval by capability

> Part of `investigate`. Use the capability needed, not a provider or tool
> name. No MCP connector is required or preconfigured.

## Discover the available route

Inspect the tools available in the current session. Prefer a specialized source
or repository tool when it provides exact text and provenance. Otherwise search
the web and open the source through an available document or fetch tool. A local
HTTP client is another option only when execution and network access exist.
Without retrieval, use inspected supplied material and flag the unavailable
coverage; model recall does not replace a primary source read.

| Need | Possible route |
|---|---|
| Cryptographic preprints | ePrint source pages, literature connector, or domain-constrained search |
| Normative specifications and status | Official standards pages, revision histories, and PDFs |
| Broader scholarly literature | DOI/publisher pages, scholarly search, citation tools |
| Related or citing work | Bibliographies, citation graphs, and follow-up searches |
| Non-paper sources | Official comments, forums, workshop pages, and issue trackers |
| Implementations and PoCs | Repository search and exact revision inspection |
| Paper or page body | Native reader, fetched HTML, PDF tools, or supplied document |

Literal tool names in older domain examples illustrate these capabilities.
Translate them to exposed interfaces; never assume a name denotes an available
API. Refresh the host's inventory once if a configured name no longer resolves.

**An abstract is not a paper.** Search results identify candidates; they rarely
establish exact preconditions, models, constants, or scope. Open the body and
record a theorem, algorithm, table, page, section, code revision, or normative
locator before using a source as load-bearing evidence.

## Recover from connector failure without looping

- **Tool name not found:** refresh the live tool inventory once and select the
  equivalent capability.
- **Repeated transport, authorization, or server failure:** stop that route
  after the repeated identical failure, preserve the diagnostic, and try one
  materially distinct connector or fetch route.
- **All routes fail:** mark the source class and affected claims `BLOCKED`, flag
  them to the user, and continue only with work independent of that evidence.

Do not turn a transient failure into a permanent global ignore rule. Keep it as
a retriable, dated entry in the investigation record. Do not issue a large batch
of calls after the same failure has already established that the route is down.

## Read PDFs as documents, not just text

Prefer trustworthy HTML or connector-provided full text when available. If the
source is PDF-only, use the host's PDF reader or available local PDF library or
CLI. Preserve page numbers and extraction provenance.

Text extraction is not authoritative for equations, tables, diagrams, or
pseudocode. Render the relevant pages and inspect the page images with an
available vision-capable model or document tool, then cross-check them against
the extracted text. If neither reliable extraction nor page inspection is
available, mark those portions `BLOCKED` rather than reconstructing them from
memory.

## Fetch responsibly

Prefer a connected fetch tool because it can apply its own network policy,
redirect handling, caching, and request headers. When using a direct HTTP client,
send a descriptive non-empty `User-Agent`, follow redirects deliberately, and
retain the final URL and response status. A publisher-specific rejection is a
reason to try an official mirror or another available route, not evidence that
the document does not exist.

## Cover the open-web gap

Much competition cryptanalysis appears only in forum posts, official comments,
workshop slides, issue trackers, or submission pages. A preprint-corpus miss is
therefore not a prior-art result. For a named competition candidate, cover:

1. official standards or round-status records;
2. forum, comment, announcement, and implementation channels;
3. the scholarly and preprint literature.

A negative is a claim about the search and must name its queries, aliases,
channels, dates, exclusions, and blocked routes.

## Keep compute and retrieval separate

Literature connectors need not provide estimators or compute hosts.

Use [`computation.md`](computation.md) to select among local programs, managed
environments, and configured remote compute. The names below describe the
requirements of particular costing paths.

- For costing, use `analyze-scheme`'s `scripts/sweep.py` only when SageMath and
  `cryptographic_estimators` are available. Otherwise mark the row `NOT CHECKED`
  and name the missing model.
- For large algebra, use the host's configured compute provider when available;
  otherwise preserve the computation as blocked work.

Prefer the narrowest tool that answers the question. Broad crawlers, monitoring
jobs, and autonomous web agents are not ordinary first-line retrieval tools.
