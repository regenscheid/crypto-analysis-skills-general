# crypto-analysis-skills-general

Portable instructions for rigorous cryptanalysis and cryptographic formal methods,
for web chats, desktop assistants, and coding agents. Use them through a native
Agent Skills loader, as files read by an agent, or as selected text supplied in a
conversation. A particular model, tool API, MCP server, filesystem, or execution
environment is never a prerequisite to reading and using the methods.

This is a general-purpose derivative of
[crypto-analysis-skills](https://github.com/regenscheid/crypto-analysis-skills).
It preserves the original Git history and all 162 methods. Generic core workflow
names use a `crypto-` prefix to reduce conflicts with other installed packs;
specialist skill IDs remain unchanged. This fork is maintained separately.

## Start here

For a chat with no repository access, paste [START_HERE.md](START_HERE.md) and
supply the relevant skill files, target specification, and evidence. For an
agent that can read this checkout, use:

> Read START_HERE.md and skills/crypto-investigate/SKILL.md. Use the relevant methods in
> this repository to analyze [target and question]. Determine which files and
> tools you can actually access. Continue with the available evidence and mark
> any missing sources, execution, or checks explicitly.

Choose a small set of skills for the assignment. Installing the entire catalog
is optional. Start with `crypto-investigate` for a broad investigation,
`crypto-analyze-paper` for a paper audit, `crypto-verify-claim` for one claim, or
`mathematical-research-development` for a stated mathematical question.
`crypto-investigate` can select symmetric, public-key, and formal-method
workflows when their files are available; it also works with a partial catalog. A missing skill
is reported as unavailable, never as loaded or as a completed check.

## Use in different environments

### Web and desktop conversations

There are two routes:

- **Native skills, when supported:** upload the selected skill folders using
  your product's skill interface. `tools/package_skills.py` produces a separate
  ZIP for each skill, each with one top-level skill folder. Enable or load only
  what is relevant. A native loader may expose only the uploaded skill, without
  access to sibling skills.
- **Ordinary chat:** attach or paste the selected Markdown instructions and
  references. The generated `context.md` packet includes those resources with
  their original paths. Ask the assistant to use them explicitly. Attaching a
  ZIP is useful only if the current session can unpack and read it; a repository
  URL or attachment alone does not establish that any file was read.

For ChatGPT, use whichever skill, file, or project interface is present in your
account. The text route works without assuming a native skill installer. Desktop
apps can have different capabilities from coding sessions on the same machine.
See the [OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills)
and [Anthropic skill documentation](https://support.claude.com/en/articles/12512180-use-skills-in-claude)
for current native support. Product interfaces and account availability can change.

### Coding agents and research platforms

An agent with file access can read the checkout directly without installing
anything. For native discovery, install **whole skill directories**, with
references and scripts, side by side in one skills directory, so the `../`
links between skills resolve. Each supported host has a short note, read only
on that host, mapping the pack's capabilities to the host's tools and saying
where results are kept; `crypto-investigate` says how to recognise each host
from the tools a session offers:

| Host | Install | Note |
|---|---|---|
| Claude Code | `.claude/skills/<name>/` or `~/.claude/skills/<name>/`, or the plugin marketplace from `package_skills.py --host claude-code` | [claude-code.md](skills/crypto-investigate/reference/hosts/claude-code.md) |
| Codex | `.agents/skills/<name>/` or `~/.agents/skills/<name>/` (`package_skills.py --host codex`) | [codex.md](skills/crypto-investigate/reference/hosts/codex.md) |
| Cryptography Atlas | `skills import --archive` of `package_skills.py --host atlas` | [cryptography-atlas.md](skills/crypto-investigate/reference/hosts/cryptography-atlas.md) |

The Claude Code and Codex notes state only what those vendors' documentation
said when checked (the pages and the date are in each note). Both load the
names and descriptions of every installed skill up front within a budget, so
installing all 162 skills shortens or drops descriptions: install the starter
set and add a domain when the work needs it. Other hosts may use other paths.
Resolve relative resources from the loaded skill's location, not an assumed
working directory. Avoid installing another copy if the same canonical skill is
already present.

### Upgrade the core workflow names

The following canonical names replace the original generic names:

| Previous name | Current name |
|---|---|
| `investigate` | `crypto-investigate` |
| `analyze-paper` | `crypto-analyze-paper` |
| `analyze-scheme` | `crypto-analyze-scheme` |
| `verify-claim` | `crypto-verify-claim` |
| `validate-attack` | `crypto-validate-attack` |
| `derive-cost` | `crypto-derive-cost` |
| `magma` | `crypto-magma` |
| `workbench-knowledge` | `crypto-workbench-knowledge` |

Install the complete updated pack, including references and scripts. Remove only
this pack's previous copies of the renamed directories from your host's skill
location; do not remove another pack's skill with the same name. Update or retire
an account-synced copy through the account's skill interface rather than deleting
its cached folder. A name such as `anthropic-skills:investigate` identifies an
account-synced skill and does not by itself identify a built-in. If the same pack
was installed locally and through account sync, check both copies. A source-
checkout rename does not remove an already installed copy. Start a fresh session
after the upgrade and check the resolved path of the skill.
Use `/crypto-investigate` in slash-command hosts or `$crypto-investigate` in Codex.

A reported invocation failure for the previous `investigate` name motivated this
change. It does not establish that a collision caused that host's rejection.
The documented visibility rules treat missing overrides as enabled; the affected
launcher and its effective settings must be checked in that environment. See
[invocation settings](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings)
and [name resolution](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name).
This pack supplies no host visibility overrides, and renaming does not override
an intentional host restriction. If invocation is denied, retain the exact
requested name, resolved path, host version, and error for diagnosis.

External consumers should migrate the old IDs using
[the explicit rename record](config/skill-migrations.json) and pin the new registry
with its source commit. No runtime aliases for the old names are installed.

### Make upload and text bundles

Packaging needs Python 3.10+ and only its standard library:

```sh
python3 tools/package_skills.py --profile starter --output dist/starter
python3 tools/package_skills.py --profile symmetric --output dist/symmetric
python3 tools/package_skills.py --skill crypto-verify-claim --output dist/one-claim
python3 tools/package_skills.py --profile starter --host claude-code --output dist/claude-code
python3 tools/package_skills.py --profile starter --host codex --output dist/codex
python3 tools/package_skills.py --profile all --host atlas --output dist/atlas
```

Without `--host`, each output directory contains `skills/<name>.zip` (one
top-level skill folder each), `context.md`, and a manifest with skill IDs and
file hashes. A single-skill ZIP cannot carry the files it links to in other
skills; the manifest lists them and `context.md` includes them. With `--host`,
the output is a whole-pack layout for that host, and every skill a selected
skill links to is added so links resolve. The starter selection contains the
core workflows and domain entry points, with `crypto-workbench-knowledge` except
for Atlas (which keeps results in its ledger) and without `crypto-magma`;
`symmetric`, `public-key`, `formal`, and `all` add a domain or everything. Large selections can exceed
an assistant's context window. Use individual skills for focused questions.
Generated bundles are ignored by Git. Packaging does not install skills, execute
their scripts, or configure any connector.

## What is included

The catalog contains 11 core workflows, 29 symmetric cryptanalysis skills,
59 public-key cryptanalysis skills, and 63 formal-method skills. Names shared
between imported packs retain `symmetric-` or `public-key-` prefixes. The generated
[skill registry](config/skill-registry.json) lists every canonical ID and domain,
and each domain router lists its specialist skills in a generated family table
([symmetric](skills/symmetric-cryptanalysis-orchestrator/references/skill-family.md),
[public-key](skills/public-key-cryptanalysis-orchestrator/references/skill-family.md),
[formal](skills/formal-methods-router/references/skill-family.md)).

The methods preserve target and attacker models, source provenance, concrete
cost accounting, bounded negative results, and distinctions among proofs,
exact checks, empirical observations, and unresolved claims. Formalization is
optional; prose or an unreplayed proof file is never machine-checked evidence.

## Capability-based behavior

| Available capability | How to work | Without it |
|---|---|---|
| Skill loader or readable files | Read selected bodies and relevant resources | Use supplied text; identify missing procedures |
| Browsing or research connectors | Open primary sources and record exact locators | Use inspected supplied material; flag current/prior-art gaps |
| Code execution | Check tools and versions in the actual execution context | Give derivations or runnable code explicitly labeled unexecuted |
| SageMath, estimators, solvers, or provers | Use only when installed and suitable | Mark the relevant cost or proof obligation `NOT CHECKED` or `BLOCKED` |
| Licensed Magma | Use a configured local or remote installation | Choose a suitable available alternative or leave the computation blocked |
| The host's own record of results (a ledger, project memory) | Record results there; do not keep a second record | — |
| Writable files but no host record | Keep results with `crypto-workbench-knowledge` (Python/POSIX helpers) in a directory the user names | Return a research handoff in the conversation; make no persistence claim |
| Authorized independent workers | Optionally split work and review fixed returns | Work sequentially; describe a self-check accurately |

Read [the environment guide](skills/crypto-investigate/reference/environment.md) for
resource loading, fallbacks, where results are kept, and resumption, and
[the retrieval reference](skills/crypto-investigate/reference/tools.md) for the
order in which to look for sources (a curated paper library first, then ePrint,
NIST publications, and general search) and the current names of the research
services' tools. No connector endpoint, remote host,
operating system, project ID, artifact API, approval UI, or subagent profile is
preconfigured by this repository. The external attack catalog is optional;
primary sources and supplied artifacts can be used directly.

The dedicated runtime adapter, internal planning and artifact calls, model alias
mapping checks, deployment-specific compute wrappers, and the upstream
application's delegation fields and permission model have been removed;
`tools/audit_skills.py` fails if they return. No skill requires the note
helpers: the core skills check what is established and record results in the
host's own record when it has one, otherwise with `crypto-workbench-knowledge`
and its research board, otherwise in a text handoff. Long research loops respect
the user's scope and the current session's limits.

## Maintainer layout and validation

| Path | Purpose |
|---|---|
| `skills/` | Runtime instructions, references, assets, and optional helpers |
| `config/imported-skills.json` | Original source provenance and installed content hashes for 151 imported skills |
| `config/skill-registry.json` | Generated canonical skill IDs for external consumers |
| `config/skill-migrations.json` | Explicit previous-to-current core skill IDs; not runtime aliases |
| `config/audit-terms.json`, `config/route-budget.json` | Terms the audit rejects, phrases it requires, and the ordinary routes it measures |
| `reports/skill-inventory.json` | Generated inventory, links, descriptions, and portability audit |
| `tests/` | Host-neutral load probe, manual behavior cases, and Python regressions |
| `tools/` | Audit, packaging, import, and offline evaluation utilities |
| `.skill-packs/` | Optional ignored source-pack staging; not an installable runtime |

Run from the repository root:

```sh
python3 tools/import_skill_packs.py --check
python3 tools/audit_skills.py
python3 tools/family_tables.py --check
python3 -m unittest discover -s tests -v
(cd skills/crypto-workbench-knowledge && python3 scripts/knowledge.py --selftest)
(cd skills/crypto-workbench-knowledge && python3 scripts/board.py --selftest)
```

The audit also guards against retired tool names and wording (a mode declared
as a label, the old rules for marking a computation blocked), the upstream
product's names and fields, unregistered skill names, broken links and anchors,
descriptions over 300 characters, host notes naming undocumented tools, and
ordinary routes over the load budget in `config/route-budget.json`. It also
fails when a file loses a phrase it must keep, such as library first where a
skill speaks of sources or how to recognise each host. Regenerate the routers'
family tables with `python3 tools/family_tables.py` after adding or renaming a
skill.

These check packaging and repository invariants; they do not establish model
behavior or scientific correctness. Use [portability cases](tests/portability-cases.json)
and [the evaluation contract](tests/evaluation-contract.md) for manual host trials.
No live trials across every product are implied by these checks.

After deliberately editing an imported skill, review its diff, run
`python3 tools/import_skill_packs.py --accept-installed-changes`, then rerun both
validators. This preserves the source hash and records local divergence. The
importer can also reconstruct staged packs from `.skill-packs/`; refreshing into
an empty destination avoids overwriting reviewed changes. Regenerate the registry
and inventory with `audit_skills.py` whenever skills change.

The attack catalog lives separately. Pin this fork's registry and commit when
validating external skill references; catalog subject links neither load a skill
nor prove an attack's applicability. Specialist IDs remain stable; the core
renames are recorded in `config/skill-migrations.json`. The catalog's current
pin predates the `crypto-` renames, so it may reject a `crypto-` ID that it
knows under the earlier name until it is re-pinned to this registry.
Retain upstream provenance and existing per-skill license metadata when reusing
or modifying imported material.
