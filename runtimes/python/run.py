"""
Janus workspace entrypoint — minimal runnable example.

Usage:
    python3 runtimes/python/run.py

Expected output:
    E+: ['step_a']
    E-: []
    HUMAN_DECISION recorded.
    Evidence file: runtimes/python/janus/janus_events.jsonl
"""

import os
import sys

# Add SDK to path
sys.path.insert(0, os.path.dirname(__file__))

import janus

# Clear previous run
events_file = os.path.join(os.path.dirname(__file__), "janus", "janus_events.jsonl")
if os.path.exists(events_file):
    os.remove(events_file)

# --- Governed workflow ---

# 1. Declare what you expect to happen
janus.expect("step_a")

# 2. Trace that it happened
janus.trace("step_a")

# 3. Evaluate: did everything expected actually occur?
janus.evaluate()

# 4. Record a human decision
janus.human_decision(
    decision="proceed",
    rationale="step_a completed successfully — evidence confirmed"
)

print("HUMAN_DECISION recorded.")
print(f"Evidence file: {os.path.relpath(events_file)}")
