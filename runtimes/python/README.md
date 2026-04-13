# Janus Python Runtime — Minimal Stub

Reference: https://framework.janusgovernance.org

---

## Run

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

## What this does

1. Declares an expected event (`expect`)
2. Records that it happened (`trace`)
3. Evaluates E+ / E− (`evaluate`)
4. Writes a `HUMAN_DECISION` governance event

The evidence file (`janus_events.jsonl`) is append-only and human-readable.

## Full SDK

→ https://github.com/Janus-Governance/janus-framework-stack/tree/main/runtimes/python-sdk
