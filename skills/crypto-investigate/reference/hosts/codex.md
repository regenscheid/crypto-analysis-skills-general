---
host: codex
checked: 2026-11-27
sources:
  - https://learn.chatgpt.com/docs/build-skills
  - https://learn.chatgpt.com/docs/config-file/config-reference
  - https://developers.openai.com/plugins/build/plugins
  - https://learn.chatgpt.com/docs/developer-commands?surface=cli
  - https://learn.chatgpt.com/docs/agent-configuration/subagents
  - https://learn.chatgpt.com/guides/best-practices
  - https://learn.chatgpt.com/docs/extend/mcp
  - https://learn.chatgpt.com/docs/agent-configuration/agents-md
tools: []
terms: [crypto-workbench-knowledge, crypto-investigate, skill-installer]
---

# Host note: Codex

Read this only when running in OpenAI's Codex (CLI, IDE extension or app).
Everything below was checked against the documentation listed in this file's
front matter on 2026-11-27 (several `developers.openai.com/codex` pages now
redirect to `learn.chatgpt.com`); where the documentation did not say, this note
says so. It names no model-facing tool, because the user documentation names
none for these capabilities.

| Capability | In Codex |
|---|---|
| Plan and progress | Plan mode (`/plan`, or Shift+Tab), in which Codex proposes a plan before implementing. A user-facing task-list tool is not described in the user documentation; keep a short written plan otherwise. |
| Delegation and independent review | Subagents, which Codex starts when asked to or when AGENTS.md or a skill says to; settings under `[agents]` in `config.toml`, custom agents as TOML files in `~/.codex/agents/` or `.codex/agents/`. Send a worker the fixed target, evidence and expected return; a subagent is a separate context, not by itself an independent reviewer of a different kind. |
| Questions to the user | The documentation says Codex asks clarifying questions in plan mode; no question tool is documented. Ask in the reply when a decision is the user's. |
| Durable record | Codex keeps no ledger of claims and evidence, so **`crypto-workbench-knowledge` is the record**, in a directory of the project the user names or agrees to. Set `CRYPTO_FILES` to that absolute path (or pass it to the helpers); they stop with a message if it is unset or not writable. Without it, use the repository's files or the conversation. |
| Artifacts | Files in the working tree. |
| Execution and long jobs | The session's shell, subject to its approval policy (skill scripts can have their own approval setting). Long-job facilities are not covered in this note. |
| Literature | MCP servers under `[mcp_servers.<name>]` in `~/.codex/config.toml` or a trusted project's `.codex/config.toml`, or `codex mcp add`; `/mcp` shows their status. See [the retrieval reference](../tools.md). |

## How Codex finds and loads skills

- **Locations.** Repository skills: `.agents/skills/` in every directory from
  the working directory up to the repository root. Personal skills:
  `~/.agents/skills/`. Administrator skills: `/etc/codex/skills`. System skills
  ship with Codex. Symlinked skill folders are followed. Two skills with the
  same `name` are not merged and can both appear; the documentation states no
  precedence, so install one copy of each skill.
- **Front matter.** `name` and `description` are required. OpenAI's page states
  no length limits and links the Agent Skills specification; this pack keeps
  names to 64 lowercase letters, digits and hyphens and descriptions to 300
  characters. An optional `agents/openai.yaml` sets display details and
  `policy.allow_implicit_invocation`; this pack ships none.
- **Listing budget.** At start Codex sees each skill's name, description and
  path; the full `SKILL.md` loads only when Codex uses the skill. The initial
  list is capped at 2% of the context window (8,000 characters when the window
  is unknown); with many skills, descriptions are shortened first and then
  skills may be left out with a warning. `skills.max_context_tokens` changes
  the budget. Installing all 162 skills will shorten descriptions: install the
  recommended set below and add specialists as needed.
- **Supporting files.** The documentation names `scripts/`, `references/` and
  `assets/` folders; this pack's folders are `reference/`, `references/`,
  `scripts/` and `assets/`, read by the paths `SKILL.md` gives. The documentation
  does not say how relative links resolve; this pack's `../` links between
  skills resolve when the whole pack is installed side by side in one
  `.agents/skills/` directory.
- **Invoking.** Codex picks a skill by its description, or the user names it
  with `$skill-name` or picks it from `/skills`. A skill is turned off with a
  `[[skills.config]]` entry (`name` or `path`, and `enabled = false`) in
  `~/.codex/config.toml`. The bundled `$skill-installer` installs skills from
  other repositories.
- **Plugins.** A Codex plugin carries `skills/<name>/SKILL.md` and a manifest
  (`.codex-plugin/plugin.json`, or a root `plugin.json`); a repository
  marketplace is `.agents/plugins/marketplace.json`, added with
  `codex plugin marketplace add owner/repo`. `tools/package_skills.py --host
  codex` writes the whole-pack `.agents/skills/` layout; it does not build a
  plugin.
- **Instruction files.** Codex reads `AGENTS.md` (or `AGENTS.override.md`) from
  `~/.codex` and from each directory from the Git root down to the working
  directory, closer files later, up to `project_doc_max_bytes` (32 KiB by
  default) in total. A project can point Codex at `crypto-investigate` there.

## Recommended set

Install the core workflows and routers (the `starter` profile, which includes
`crypto-workbench-knowledge` for this host) and add a domain's specialist skills
when the work needs them (`--profile symmetric`, `public-key` or `formal`).
