# Janus Workspace Template

A minimal, runnable starting point for Janus-governed workspaces.

→ Framework: https://framework.janusgovernance.org
→ Core: https://github.com/Janus-Governance/janus-governance-core

---

## Operational Quick Start

### Step 1 — Run something

```sh
python3 runtimes/python/run.py
```

Expected output:

```
E+: ['step_a']
E-: []
HUMAN_DECISION recorded.
Evidence file: runtimes/python/janus/janus_events.jsonl
```

### Step 2 — Produce evidence

```sh
cat runtimes/python/janus/janus_events.jsonl
```

Each line is a governance event. The file is append-only.

---

## Structure

```
janus-workspace-template/
├── dev/            # active development work
├── core/           # references to Janus Core (read-only)
├── runtimes/
│   └── python/     # minimal Python runtime + SDK stub
├── protocol/       # 8 protocol stubs → framework.janusgovernance.org
├── rfcs/           # local RFC drafts
└── observability/  # monitoring stub
```

---

## What Janus does

- Makes decisions traceable (HUMAN_DECISION)
- Records evidence explicitly (E+ / E−)
- Detects omissions (OMISSION_DETECTED)
- Enforces human authority where required

---

## Next steps

1. Replace `step_a` in `run.py` with your actual workflow steps
2. Add your governed logic in `dev/`
3. Extend protocol stubs in `protocol/` as needed
4. Push evidence to your audit log

Full documentation: https://framework.janusgovernance.org
