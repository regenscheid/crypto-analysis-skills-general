# Research retrieval by capability

> Part of `crypto-investigate`. This is the one retrieval reference for the pack;
> the object-level skills and `crypto-review` point here instead of carrying their
> own tool lists. Use the capability needed, not a provider or tool name. No
> connector is required or preconfigured.

## Look in this order

Inspect the tools the current session actually offers, then use the first route
that serves the need:

1. **A curated library of papers with page-level reading**, if the environment
   has one. Find the paper there first; read the pages that carry the result;
   search inside the held text for the phrase or theorem number you need. A
   library entry's summary card is a description written by someone else, not
   the paper: never quote it.
2. **The IACR ePrint archive** for preprints the library does not hold: search
   its metadata, find a phrase in one paper's body, then read whole pages.
3. **NIST publications** for standards, status reports and their revisions:
   resolve the exact edition, find passages, read pages.
4. **General search and fetch** for what is not a paper: forum posts, official
   comments, workshop pages, implementation repositories, issue trackers,
   errata pages, and publisher pages with a DOI.

Without any retrieval, use inspected supplied material and flag the unavailable
coverage; model recall does not replace a primary source read.

**Quotes come from the page actually read**, whatever the source: copy the words
exactly from one page or passage returned in this session, with its locator
(physical page or printed page, section, theorem number, revision or edition,
URL and retrieval date). Do not join text across a page break, a header, or a
summary. A paraphrase is labeled as one.

| Need | Route by capability |
|---|---|
| Find a paper on a topic | Library search, then ePrint search, then scholarly search |
| Read a paper's body | Library page reader; ePrint full-text pages; a PDF or HTML reader |
| Find a phrase or theorem inside one paper | Library or ePrint in-paper search, then read that page |
| A paper's theorems and definitions | Library statement extraction, then read the page each is on |
| Related or citing work | Library citation graph; scholarly citation tools; bibliographies |
| Normative specifications and status | NIST edition lookup and page reader; official standards pages |
| Non-paper sources | Web search and page fetch |
| Implementations and PoCs | Repository search and exact revision inspection |
| Attack records and their sources | The optional attack catalog (see [catalog use](catalog-use.md)) |

## If these servers are connected, their tools are

These are the tool names of the research services this pack was most recently
checked against (2026-11-27). Hosts show them in different forms: a gateway may
prefix the server name (`library-mcp_find_papers`), and some hosts use their own
form (for example `mcp__<server>__<tool>`). They are examples of the capabilities
above, not prerequisites; use whatever equivalent the session offers.

| Server | Tool | Use |
|---|---|---|
| `library-mcp` | `find_papers(query)` | One search over the library, ePrint and scholarly indexes; says what is held |
| | `read_paper(identifier, start_page, page_count)` | Read held text as whole pages (physical page numbers, 1–5 pages a call) |
| | `search_in_paper(identifier, phrase)` | Find a literal phrase in one held text; returns page numbers |
| | `paper_statements(identifier, kind)` | The paper's numbered theorems, lemmas and definitions, each with its page |
| | `paper_references(identifier)` | The paper's reference list, resolved where possible |
| | `related_papers(identifier, relation)` | Papers citing it (`cited_by`) or cited by it (`cites`) |
| `e-print-mcp` | `search_eprint(query)` | Search ePrint metadata |
| | `search_eprint_fulltext(paper_id, query)` | Find a phrase in one paper's body; returns page numbers |
| | `eprint_fulltext(paper_id, start_page, page_count)` | Read the body as whole pages |
| | `get_eprint(paper_id)` | Metadata and abstract only |
| `nist-csrc-mcp` | `nist_search(query, kind)` | Find publications (`kind="publications"`) or page passages (`kind="passages"`) |
| | `nist_get_publication(query="FIPS 203")` | Resolve an edition: status, revisions, drafts, supersession |
| | `nist_read(edition_id, page_index or printed_page)` | Read pages of one edition |
| `paper-search-mcp` | `search_papers`, `paper_details`, `paper_citations` | Scholarly indexes beyond the library |
| `web-fetch-mcp` | `web_fetch`, `fetch_page` | Fetch one page for reading |
| `firecrawl-mcp` | `firecrawl_search`, `firecrawl_scrape` | Web search for non-paper sources; scrape one page |
| `attack-catalog-mcp` | `search_attacks`, `get_attack`, `list_attacks_for_skill`, `get_catalog_info` | Optional attack records; see [catalog reading](catalog-reading.md) |

Tool names change. Refresh the host's inventory once if a name no longer
resolves, and select the equivalent capability; never assume a name denotes an
available API.

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
- **A paper not yet held:** some readers queue a fetch and say to read again
  later. Come back on a later pass rather than concluding the body is
  unreachable; if it stays unreachable, mark the dependent parameterisation
  unverified.
- **All routes fail:** mark the source class and affected claims `BLOCKED`, flag
  them to the user, and continue only with work independent of that evidence.

Do not turn a transient failure into a permanent global ignore rule. Keep it as
a retriable, dated entry in the investigation record. Do not issue a large batch
of calls after the same failure has already established that the route is down.

## Read PDFs as documents, not just text

Prefer page-level text from a library or connector when available. If the
source is PDF-only, use the host's PDF reader or an available local PDF library or
CLI. Preserve page numbers and extraction provenance.

Text extraction is not authoritative for equations, tables, diagrams, or
pseudocode. Render the relevant pages and inspect the page images with an
available vision-capable model or document tool, then cross-check them against
the extracted text. A reader that flags lost mathematics on a page is telling
you to open the original. If neither reliable extraction nor page inspection is
available, mark those portions `BLOCKED` rather than reconstructing them from
memory.

## Fetch responsibly

Prefer a connected fetch tool because it can apply its own network policy,
redirect handling, caching, and request headers. When using a direct HTTP client,
send a descriptive non-empty `User-Agent`, follow redirects deliberately, and
retain the final URL and response status. A publisher-specific rejection is a
reason to try an official mirror or another available route, not evidence that
the document does not exist. Keep the body of a failed response: a status code
without its body discards the diagnosis.

## Cover the open-web gap

Much competition cryptanalysis appears only in forum posts, official comments,
workshop slides, issue trackers, or submission pages. A preprint-corpus miss is
therefore not a prior-art result. For a named competition candidate, cover:

1. official standards or round-status records (for NIST's post-quantum process,
   the round status reports IR 8240, 8309, 8413, 8528 and their successors say
   why a scheme did not advance);
2. forum, comment, announcement, and implementation channels;
3. the scholarly and preprint literature.

A negative is a claim about the search and must name its queries, aliases,
channels, dates, exclusions, and blocked routes.

## Keep compute and retrieval separate

Literature services need not provide estimators or compute hosts.

Use [`computation.md`](computation.md) to select among local programs, managed
environments, and configured remote compute. The names below describe the
requirements of particular costing paths.

- For costing, use `crypto-analyze-scheme`'s `scripts/sweep.py` only when SageMath and
  `cryptographic_estimators` are available. Otherwise mark the row `NOT CHECKED`
  and name the missing model.
- For large algebra, use the host's configured compute provider when available;
  otherwise preserve the computation as blocked work.

Prefer the narrowest tool that answers the question. Broad crawlers, monitoring
jobs, and autonomous web agents are not ordinary first-line retrieval tools.
