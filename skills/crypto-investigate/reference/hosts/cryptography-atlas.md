---
host: cryptography-atlas
checked: 2026-11-27
source: the platform's own code and docs (skills, delegation, plan, ledger, memory and job tools)
tools: [plan_create, plan_activate, plan_progress, plan_revise, plan_finish, plan_read, track_read, track_progress, delegate, wait_delegations, delegation_status, cancel_delegation, accept_delegation, message_child, message_parent, submit_result, ask_user, ledger_change, ledger_read, ledger_import, memory_propose, memory_list, document_create, document_patch, document_read, write_file, read_file, publish, find_artifacts, python, sage, shell, start_job, wait_jobs, mcp_tools, load_tools, skills, find_papers, read_paper, search_in_paper]
terms: [literature-search, computation, delegating-work, recording-results, crypto-workbench-knowledge]
---

# Host note: Cryptography Atlas

Read this only when running on the Cryptography Atlas research platform. It maps
the pack's capabilities to the platform's tools. **The platform's built-in skills
(`literature-search`, `computation`, `delegating-work`, `recording-results`, and
the others) win wherever they differ from this pack**: for example the library
comes first for papers, and a quote comes from a single page or passage the
library returned in this session, never a summary card.

| Capability | On this platform |
|---|---|
| Plan and progress | `plan_create`, then `plan_activate`; `plan_progress` per step with evidence; `plan_revise` when premises change; `plan_finish`; `plan_read`. A delegated run reports through `track_read` and `track_progress`. |
| Delegation and independent review | `delegate` with either a **task** or a **check** of a ledger entry. For a check the platform writes the checker's framing and lists the entry's evidence itself; you add only a note, never the expected verdict. A task never counts as an independent check. Then `wait_delegations`, `delegation_status`, `message_child`, and `accept_delegation`; a worker ends with `submit_result` and can reach its parent with `message_parent`. The platform also runs its own consistency reviews. |
| Questions to the user | `ask_user`, with two to four options; a run may ask only a few, and delegated runs cannot ask. |
| Durable record | **The ledger is the record of claims and evidence**: `ledger_change` to propose or update entries, `ledger_read` to check what is established, `ledger_import` for results files written by code. Project memory (`memory_propose`, `memory_list`) holds standing context, not results. Documents (`document_create`, `document_patch`, `document_read`) hold reports. `crypto-workbench-knowledge`, its files and its board are **not used here**. |
| Artifacts | `write_file` and `read_file` in the workspace, `publish` to show a file, `find_artifacts` to find one. |
| Execution | `python`, `sage`, `shell`. Long work: `start_job` and `wait_jobs`, offered after `load_tools` loads the jobs group. |
| Connectors and literature | `mcp_tools` lists and loads connector tools; `load_tools` loads further groups. Papers: the library first (`find_papers`, `read_paper`, `search_in_paper`), then the other services in [the retrieval reference](../tools.md). |

## How the platform loads this pack

- The platform imports the pack and shows each run an **index of skill names and
  descriptions** (about 12,000 characters for all packs together; long
  descriptions are cut, and past the budget skills are listed by name only). A
  description therefore has to say what the skill is for in its first sentence.
- The run loads bodies on demand with the `skills` tool (`search`, `load`,
  `read`; `read` reaches a sibling skill's file through `../` inside the pack).
  **A run may load at most about 100,000 characters of skill text**, bodies and
  read files together. Load `crypto-investigate`, one object-level skill and the
  two or three references the step needs; do not read every reference up front.
- A pack whose skill folder holds more than Markdown is **staged read-only** in
  the environment when such a skill loads; the load's answer says where. Run a
  helper (for example `crypto-analyze-scheme`'s `scripts/sweep.py`) from that
  staged path and write its outputs to the workspace, never into the staged
  folder. Environment variables for a pack are set only when the platform's
  import pass derived them and the project allows them; do not rely on them.
- Do not reproduce the pack's own record-keeping here: record results in the
  ledger as `recording-results` describes.
