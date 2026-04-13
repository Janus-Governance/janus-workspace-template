# Protocol 07 — Runtime Intervention

**Status:** stub  
**Ref:** https://framework.janusgovernance.org/protocol/runtime-intervention-rules

---

## Principle

When a runtime detects a governance violation, it must stop and surface evidence.  
It must not silently continue or self-correct without human authorization.

## Required events

- `INTERVENTION` — records what was detected and why execution was halted
