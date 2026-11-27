---
host: claude-code
checked: 2026-11-27
sources:
  - https://code.claude.com/docs/en/skills
  - https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
  - https://code.claude.com/docs/en/plugins/manifest-reference
  - https://code.claude.com/docs/en/plugins/create-marketplace
  - https://code.claude.com/docs/en/sub-agents
  - https://code.claude.com/docs/en/tools-reference
  - https://code.claude.com/docs/en/mcp
  - https://code.claude.com/docs/en/memory
tools: [Skill, Agent, TaskCreate, TaskUpdate, TaskList, EnterPlanMode, ExitPlanMode, AskUserQuestion, ToolSearch]
terms: [crypto-workbench-knowledge, crypto-investigate]
---

# Host note: Claude Code

Read this only when running in Anthropic's Claude Code. Everything below was
checked against the documentation listed in this file's front matter on
2026-11-27; where the documentation did not say, this note says so.

| Capability | In Claude Code |
|---|---|
| Plan and progress | Task-list tools (`TaskCreate`, `TaskUpdate`, `TaskList`) and plan mode (`EnterPlanMode`, `ExitPlanMode`), as the tools reference lists them; which are on depends on the version and model. |
| Delegation and independent review | Subagents, started with the `Agent` tool; definitions live in `.claude/agents/` (project) or `~/.claude/agents/` (personal). A subagent starts without the conversation: send it the fixed target, evidence and expected return. A subagent is a separate context, not by itself an independent reviewer of a different kind. |
| Questions to the user | `AskUserQuestion` (multiple-choice questions). |
| Durable record | Claude Code keeps no ledger of claims and evidence, so **`crypto-workbench-knowledge` is the record**, in a directory of the project the user names or agrees to. Set `CRYPTO_FILES` to that absolute path (or pass it to the helpers); the helpers stop with a message if it is unset or not writable. Without it, use the repository's files or the conversation. |
| Artifacts | Files in the working tree. |
| Execution | The shell tools of the session, subject to its permission settings. |
| Long jobs | Not covered in this note; run long work as the session's permissions allow and record what ran. |
| Literature | MCP servers added with `claude mcp add` (scopes local, project, user; project scope writes `.mcp.json`). Their tools appear as `mcp__<server>__<tool>`; deferred tools are loaded with `ToolSearch`. See [the retrieval reference](../tools.md). |

## How Claude Code finds and loads skills

- **Locations.** Personal skills: `~/.claude/skills/<name>/SKILL.md`. Project
  skills: `.claude/skills/<name>/SKILL.md` (also read from parent directories up
  to the repository root). Plugin skills: `<plugin>/skills/<name>/SKILL.md`,
  invoked as `/plugin-name:skill-name`. On a name clash a personal skill beats a
  project one; plugin skills are namespaced and do not clash.
- **Front matter.** `name` (defaults to the directory name) and `description`
  are the fields this pack uses; Claude Code accepts more (for example
  `allowed-tools`, `disable-model-invocation`) and ignores unknown ones. Claude
  Code truncates `description` (with `when_to_use`) at 1,536 characters in its
  listing and states no `name` limit; Anthropic's Agent Skills overview limits
  `name` to 64 lowercase letters, digits and hyphens and `description` to 1,024
  characters. This pack keeps every description to 300 characters.
- **Listing budget.** The names and descriptions of all installed skills are in
  context from the start; a body loads only when the skill is invoked (by Claude,
  or by the user typing `/skill-name`). The listing's budget is about 1% of the
  context window; when it overflows, descriptions of the least-used skills are
  dropped first and names always stay. Installing all 162 skills therefore
  costs listing space: install the recommended set below and add specialists as
  needed.
- **Supporting files.** Link references from `SKILL.md` with relative links;
  scripts are run, and only their output enters context. `${CLAUDE_SKILL_DIR}`
  names the folder that holds `SKILL.md`. The documentation does not say how
  relative links in `SKILL.md` resolve; this pack's `../` links between skills
  resolve when the whole pack is installed side by side (every skill folder in
  the same `skills/` directory).
- **Plugins.** A plugin has `skills/<name>/SKILL.md` at its root and an optional
  `.claude-plugin/plugin.json` whose only required field is `name`; a
  marketplace is `.claude-plugin/marketplace.json` listing plugins by `name` and
  `source`. Install with `/plugin marketplace add <path or owner/repo>` and
  `/plugin install <plugin>@<marketplace>`. `tools/package_skills.py --host
  claude-code` writes this layout.
- **Instruction files.** `CLAUDE.md` (personal, project, and `.claude/CLAUDE.md`)
  is read at start. The memory documentation says `AGENTS.md` is read when no
  `CLAUDE.md` is present, and can otherwise be imported from `CLAUDE.md` with
  `@AGENTS.md`. A project can point Claude at `crypto-investigate` from there.

## Recommended set

Install the core workflows and routers (the `starter` profile, which includes
`crypto-workbench-knowledge` for this host) and add a domain's specialist skills
when the work needs them (`--profile symmetric`, `public-key` or `formal`).
