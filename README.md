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

### Coding agents

An agent with file access can read the checkout directly without installing
anything. For native discovery, copy selected **whole skill directories**, with
references and scripts, to the skill location supported by your agent:

| Host | Project location | Personal location |
|---|---|---|
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` |
| Anthropic coding agent | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` |

Confirm the locations against the
[OpenAI documentation](https://learn.chatgpt.com/docs/build-skills) or
[Anthropic coding documentation](https://code.claude.com/docs/en/skills) for the
installed version. Other hosts may use other paths. Resolve relative resources
from the loaded skill's location, not an assumed working directory. Avoid
installing another copy if the same canonical skill is already present.

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
```

Each output directory contains `skills/<name>.zip`, `context.md`, and a manifest
with skill IDs and file hashes. Profiles are selections, not transitive dependency
installers: cross-skill references remain optional and are labeled when absent.
The starter selection contains the main workflows and domain entry points;
`public-key`, `formal`, and `all` are also available. Large selections can exceed
an assistant's context window. Use individual skills for focused questions.
Generated bundles are ignored by Git. Packaging does not install skills, execute
their scripts, or configure any connector.

## What is included

The catalog contains 11 core workflows, 29 symmetric cryptanalysis skills,
59 public-key cryptanalysis skills, and 63 formal-method skills. Names shared
between imported packs retain `symmetric-` or `public-key-` prefixes. The generated
[skill registry](config/skill-registry.json) lists every canonical ID and domain.

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
| Writable persistent files | Optionally use `crypto-workbench-knowledge` (Python/POSIX helpers) | Return a research handoff in the conversation; make no persistence claim |
| Authorized independent workers | Optionally split work and review fixed returns | Work sequentially; describe a self-check accurately |

Read [the environment guide](skills/crypto-investigate/reference/environment.md) for
resource loading, fallbacks, and resumption. No connector endpoint, remote host,
operating system, project ID, artifact API, approval UI, or subagent profile is
preconfigured by this repository. The external attack catalog is optional;
primary sources and supplied artifacts can be used directly.

The dedicated runtime adapter, internal planning and artifact calls, model alias
mapping checks, and deployment-specific compute wrappers from the upstream
application have been removed. The research board remains an optional Python
helper, with a text handoff when durable storage is unavailable. Long research
loops respect the user's scope and the current session's limits.

## Maintainer layout and validation

| Path | Purpose |
|---|---|
| `skills/` | Runtime instructions, references, assets, and optional helpers |
| `config/imported-skills.json` | Original source provenance and installed content hashes for 151 imported skills |
| `config/skill-registry.json` | Generated canonical skill IDs for external consumers |
| `config/skill-migrations.json` | Explicit previous-to-current core skill IDs; not runtime aliases |
| `reports/skill-inventory.json` | Generated inventory, links, descriptions, and portability audit |
| `tests/` | Host-neutral load probe, manual behavior cases, and Python regressions |
| `tools/` | Audit, packaging, import, and offline evaluation utilities |
| `.skill-packs/` | Optional ignored source-pack staging; not an installable runtime |

Run from the repository root:

```sh
python3 tools/import_skill_packs.py --check
python3 tools/audit_skills.py
python3 -m unittest discover -s tests -v
python3 skills/crypto-workbench-knowledge/scripts/knowledge.py --selftest
python3 skills/crypto-workbench-knowledge/scripts/board.py --selftest
```

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
renames are recorded in `config/skill-migrations.json`.
Retain upstream provenance and existing per-skill license metadata when reusing
or modifying imported material.
