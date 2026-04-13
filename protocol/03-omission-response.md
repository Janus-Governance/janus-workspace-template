# Protocol 03 — Omission Response

**Status:** stub  
**Ref:** https://framework.janusgovernance.org/protocol/omission-response

---

## Principle

When an expected event does not occur, this is an omission (E−).  
Omissions are recorded, not silently ignored.

## Required events

- `OMISSION_DETECTED` — written automatically by `evaluate()` when E− > 0

## Stub implementation

```python
janus.expect("critical_step")
# critical_step never traced → OMISSION_DETECTED written to janus_events.jsonl
janus.evaluate()
```
