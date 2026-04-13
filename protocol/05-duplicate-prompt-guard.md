# Protocol 05 — Duplicate Prompt Guard

**Status:** stub  
**Ref:** https://framework.janusgovernance.org/protocol/duplicate-prompt-guard

---

## Principle

Duplicate prompts produce non-deterministic outputs.  
The system must detect and block re-submission of identical prompts without re-authorization.

## Required events

- `DUPLICATE_DETECTED` — logged when a prompt ID is reused without new authorization
