# Work with the capabilities actually available

This catalog can be used in a web conversation, desktop assistant, or coding
agent. Product names do not establish tool access. Inspect the current session's
provided interfaces; do not call a guessed API to discover whether it exists.

## Instruction and reference access

Use the first available route for each relevant skill:

1. The host's native skill loader, if it exposes the skill.
2. Read its `SKILL.md` and relevant resources through file tools.
3. Read attached or pasted instruction text, including a generated context packet.

Resolve relative links from the resource's original path. A native installation
may expose just one skill directory; sibling paths are optional, not guaranteed
filesystem access. In a flattened packet, use the labeled original paths. If a
required resource is absent, identify it and continue work independent of it.
Do not fabricate its contents or list it as loaded. A named technique can still
be discussed from inspected evidence without claiming use of the missing skill.

Select workflows by the task and domain, then techniques by applicability.
Descriptions, catalog subject links, and this repository's registry are finding
aids, not execution hooks. An incomplete installed catalog need not block a
bounded question. Record whether instructions were loaded natively, read as files,
or supplied as text; do not imply native invocation from a text mention.

## Capability check

Check only what the task needs, using the host's tool inventory and a small
functionality check when appropriate. Record material limits, not a long setup
ceremony. Distinguish **available**, **unavailable**, and **unknown**.

| Capability | Evidence of availability | Fallback |
|---|---|---|
| Source retrieval | Visible browsing, document, repository, or research tools | Inspect supplied sources; state retrieval and currency limits |
| Execution | Working shell, notebook, code tool, or managed job interface | Reason from evidence; supply unexecuted scripts if useful |
| Specialist software | Version and minimal functionality check in the actual runtime | Suitable available implementation or blocked obligation |
| Durable storage | Confirmed writable path or saved host document | In-chat handoff; temporary sandbox files alone do not prove persistence |
| Independent workers | An exposed delegation interface and permission to use it | Sequential work with accurately described self-checks |

No shell, Python, SageMath, prover, internet connection, MCP endpoint, or shared
filesystem is assumed. A tool on the user's machine may be absent from the
assistant's execution sandbox. Use [computation.md](computation.md) for material
runs and [tools.md](tools.md) for source retrieval. Equivalent tools must meet the
same exactness and evidence requirements.

## Plans, storage, and resumption

For a multi-stage task, use an available plan interface or a short written plan.
Follow the current host's authorization rules; the methods do not require a
special plan-approval card. Update the plan when its premises change.

Use an existing project record if accessible. `workbench-knowledge` is optional
and its file helpers require Python, POSIX `fcntl` locking, and a writable project
directory. Use text or host documents on unsupported systems. Choose an explicit stable
project ID only when persistence is useful; reuse it across sessions. Do not
assume a home-directory convention, artifact store, version ID, or grant model.
A saved filename may overwrite a file or create a new version depending on the
host. Retain exact paths, hashes, or host version IDs where available and confirm
writes before claiming persistence. Never auto-publish results or schedule work.

Without durable storage, put the target, source versions, assumptions, evidence,
findings, open obligations, and next step in the conversation. Label this a
handoff for the user to retain. On resumption, use the supplied record and
revalidate only changed or unreliable premises.

## Optional delegation and review

Delegation is an optimization when available and authorized, never a prerequisite.
Otherwise perform the relevant phases sequentially. A review by the same model
in the same context is not an independent agent or external verification.

When using workers, send the fixed target, assumptions, exact task, evidence,
limits, and expected return. Do not assume shared memory, inherited tools,
shared paths, role names, model settings, or child approval behavior. Supply
files through the actual supported handoff route. Review returned evidence and
research significance; an agent's verdict is not proof. The optional research
board documents its own outcome fields without requiring any host SDK.

## Tool failure

Refresh an available tool inventory once for an unresolved tool name. After a
repeated identical failure, stop that route, retain its diagnostic, and try a
materially distinct available route. If all routes fail, mark affected evidence
`BLOCKED` or `NOT CHECKED`. Continue independent work with explicit limits.
A timeout, failed search, or unavailable backend is not a cryptographic result.
