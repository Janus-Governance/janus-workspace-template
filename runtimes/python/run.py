"""
Janus workspace entrypoint — minimal runnable example.

Demonstrates:
  - E+ : expected event that occurs        → governance confirmed
  - E- : expected event that does NOT occur → omission detected, audit trail written

Usage:
    python3 runtimes/python/run.py

Expected output:
    [CASE 1 — Happy path]
    E+: ['step_a']
    E-: []

    [CASE 2 — Governance gap]
    E+: []
    E-: ['step_b']
    OMISSION_DETECTED written to audit log.

    HUMAN_DECISION recorded.
    Evidence file: runtimes/python/janus/janus_events.jsonl
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import janus

# Clear previous run for a clean demo
events_file = os.path.join(os.path.dirname(__file__), "janus", "janus_events.jsonl")
if os.path.exists(events_file):
    os.remove(events_file)

# ─────────────────────────────────────────────
# CASE 1 — Happy path (E+ only)
# Expected event occurs → governance confirmed
# ─────────────────────────────────────────────
print("[CASE 1 — Happy path]")
janus.expect("step_a")
janus.trace("step_a")      # step_a happened — evidence recorded
janus.evaluate()           # E+: ['step_a']  E-: []

print()

# ─────────────────────────────────────────────
# CASE 2 — Governance gap (E- present)
# Expected event does NOT occur → omission detected
# This is what Janus exists to surface.
# ─────────────────────────────────────────────
# Reset log for a clean case
if os.path.exists(events_file):
    os.remove(events_file)
janus._EXPECTED_EVENTS.clear()

print("[CASE 2 — Governance gap]")
janus.expect("step_b")
# step_b is never traced — simulates a missing action, undocumented decision,
# or a workflow that ran but left no evidence
janus.evaluate()           # E+: []  E-: ['step_b'] → OMISSION_DETECTED written
print("OMISSION_DETECTED written to audit log.")

print()

# ─────────────────────────────────────────────
# Human authorizes continuation despite omission
# ─────────────────────────────────────────────
janus.human_decision(
    decision="proceed_with_known_gap",
    rationale="step_b omission acknowledged — proceeding under human authority"
)

print("HUMAN_DECISION recorded.")
print(f"Evidence file: {os.path.relpath(events_file)}")
