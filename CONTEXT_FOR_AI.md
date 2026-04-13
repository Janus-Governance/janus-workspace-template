# CONTEXT_FOR_AI.md

This file provides governance context for AI agents operating inside this workspace.
It follows the Janus evidence-first protocol.

→ Framework: https://framework.janusgovernance.org
→ Core: https://github.com/Janus-Governance/janus-governance-core

---

## 1. Workspace Identity

**Project:**         [your project name]
**Owner:**           [your name / org]
**Purpose:**         [one line — what this workspace governs]
**Governed since:**  [date]

---

## 2. Janus Protocol in Effect

This workspace operates under the following protocols:

| # | Protocol | Status |
|---|---|---|
| 01 | Evidence-First | active |
| 02 | Human Gate | active |
| 03 | Omission Response | active |
| 04 | Prompt Governance | active |
| 05 | Duplicate Prompt Guard | active |
| 06 | Core Protection | active |
| 07 | Runtime Intervention | active |
| 08 | Audit Log Model | active |

Full definitions: `protocol/` or https://framework.janusgovernance.org/protocol/

---

## 3. Operating Rules for AI Agents

1. **Evidence first.** Collect and present evidence before proposing any action.
2. **No action without authorization.** Wait for explicit human approval.
3. **Record decisions.** Every authorized action must produce a `HUMAN_DECISION` event.
4. **Do not touch** files or folders outside the declared scope unless explicitly authorized.
5. **Surface omissions.** If something expected did not happen, report it as E−. Do not silently skip.

---

## 4. Governance Log

Append entries here after significant sessions.

| Date | Session summary | Key decisions |
|---|---|---|
| [YYYY-MM-DD] | [what happened] | [what was authorized] |

---

## 5. Active Scope

**In scope:**
- `dev/`
- `runtimes/`

**Out of scope (read-only):**
- `core/` — references Janus Core, do not redefine
- `protocol/` — stubs only, canonical authority at framework.janusgovernance.org

---

## 6. Evidence File

Append-only runtime log:
`runtimes/python/janus/janus_events.jsonl`

Do not delete or modify this file. Append only.
