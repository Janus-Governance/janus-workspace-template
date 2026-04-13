# Protocol 02 — Human Gate

**Status:** stub  
**Ref:** https://framework.janusgovernance.org/protocol/human-gate-rules

---

## Principle

Certain decisions require explicit human authorization before the system proceeds.  
No autonomous bypass is permitted.

## Required events

- `HUMAN_DECISION` — records decision, rationale, and timestamp

## Stub implementation

```python
janus.human_decision(decision="proceed", rationale="evidence confirmed")
```
