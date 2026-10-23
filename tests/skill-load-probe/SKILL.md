---
name: skill-load-probe
description: Test whether supplied or natively installed skill instructions can be read and followed before an investigation. Use when explicitly asked to run the skill-load probe; the response alone does not establish native loading.
---

# Skill instruction probe

Return exactly this JSON object, with no Markdown fence or additional text:

```json
{
  "probe": "skill-load-probe",
  "body_marker": "SKILL-BODY-9D3C2A71",
  "instructions_loaded": true,
  "next": "inspect the available instruction access evidence"
}
```

Do not call research, network, or computation tools. The body marker tests
adherence to these instructions. It does not prove how the text was obtained;
native loading, file reads, and pasted text are distinct access routes.
