# Protocol 08 — Audit Log Model

**Status:** stub  
**Ref:** https://framework.janusgovernance.org/protocol/

---

## Principle

All governance events are written to an append-only log.  
The log is the ground truth. No event is deleted or overwritten.

## Log format

Each line is a JSON object with at minimum:

```json
{ "type": "...", "name": "...", "ts": "ISO8601Z" }
```

## Log types

| type | description |
|---|---|
| `trace` | something happened |
| `expect` | something was expected |
| `governance` | system-level event (OMISSION_DETECTED, HUMAN_DECISION, INTERVENTION) |

## Reference log

`runtimes/python/janus/janus_events.jsonl`
