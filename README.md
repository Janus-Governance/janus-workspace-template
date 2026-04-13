# Janus Workspace Template

[![Use this template](https://img.shields.io/badge/Use_this_template-2ea44f?style=for-the-badge)](../../generate)

A minimal, runnable starting point for Janus-governed workspaces.
Clone it, run it, produce evidence. No external dependencies.

→ Framework: https://framework.janusgovernance.org
→ Core: https://github.com/Janus-Governance/janus-governance-core

---

## Quick Start

```sh
git clone https://github.com/Janus-Governance/janus-workspace-template
cd janus-workspace-template
python3 runtimes/python/run.py
```

Expected output:

```
[CASE 1 — Happy path]
E+: ['step_a']
E-: []

[CASE 2 — Governance gap]
E+: []
E-: ['step_b']
OMISSION_DETECTED written to audit log.

HUMAN_DECISION recorded.
Evidence file: runtimes/python/janus/janus_events.jsonl
```

Then inspect the evidence:

```sh
cat runtimes/python/janus/janus_events.jsonl
```

Each line is a governance event. The file is append-only.

---

## What this demonstrates

**Case 1 — Happy path:** an expected event occurs, evidence is confirmed (E+).

**Case 2 — Governance gap:** an expected event does NOT occur. Janus surfaces this as an omission (E−) and writes an `OMISSION_DETECTED` event to the audit log. A human decision is required to proceed.

This is the core of what Janus does: it makes the gap between what should have happened and what actually happened observable and auditable.

---

## Structure

```
janus-workspace-template/
├── CONTEXT_FOR_AI.md    ← governance context for AI agents
├── dev/                 ← active development work
├── core/                ← references to Janus Core (read-only)
├── runtimes/
│   └── python/          ← minimal Python runtime + SDK stub
│       ├── run.py       ← executable entrypoint
│       └── janus/       ← SDK (no external dependencies)
├── protocol/            ← 8 protocol stubs
├── rfcs/                ← local RFC drafts
└── observability/       ← monitoring stub
```

---

## Adapt to your workflow

1. Edit `CONTEXT_FOR_AI.md` with your project identity and scope
2. Replace `step_a` / `step_b` in `run.py` with your actual workflow steps
3. Add your governed logic in `dev/`
4. Use `janus.human_decision()` wherever a human must authorize an action

---

## Protocol reference

| # | Protocol |
|---|---|
| 01 | [Evidence-First](protocol/01-evidence-first.md) |
| 02 | [Human Gate](protocol/02-human-gate.md) |
| 03 | [Omission Response](protocol/03-omission-response.md) |
| 04 | [Prompt Governance](protocol/04-prompt-governance.md) |
| 05 | [Duplicate Prompt Guard](protocol/05-duplicate-prompt-guard.md) |
| 06 | [Core Protection](protocol/06-core-protection.md) |
| 07 | [Runtime Intervention](protocol/07-runtime-intervention.md) |
| 08 | [Audit Log Model](protocol/08-audit-log-model.md) |

Full definitions: https://framework.janusgovernance.org/protocol/
