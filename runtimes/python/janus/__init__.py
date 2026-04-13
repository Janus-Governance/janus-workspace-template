"""
Janus Python SDK — minimal stub for workspace template.
Full SDK: https://framework.janusgovernance.org
"""

import json
import os
from datetime import datetime

_EVENTS_FILE = os.path.join(os.path.dirname(__file__), "janus_events.jsonl")
_EXPECTED_EVENTS = []


def trace(name, payload=None):
    """Append a trace event with optional payload."""
    event = {
        "type": "trace",
        "name": name,
        "payload": payload,
        "ts": datetime.utcnow().isoformat() + "Z"
    }
    with open(_EVENTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def expect(name):
    """Register an expected event (E+ candidate)."""
    _EXPECTED_EVENTS.append(name)
    event = {
        "type": "expect",
        "name": name,
        "ts": datetime.utcnow().isoformat() + "Z"
    }
    with open(_EVENTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")


def evaluate():
    """Compare recorded events against expected. Print E+ / E-."""
    events = set()
    expected = set()
    if os.path.exists(_EVENTS_FILE):
        with open(_EVENTS_FILE, "r", encoding="utf-8") as f:
            for line in f:
                try:
                    evt = json.loads(line)
                    if evt.get("type") == "trace":
                        events.add(evt["name"])
                    if evt.get("type") == "expect":
                        expected.add(evt["name"])
                except Exception:
                    pass
    found = events & expected
    missing = expected - events
    print(f"E+: {sorted(found)}")
    print(f"E-: {sorted(missing)}")
    if missing:
        with open(_EVENTS_FILE, "a", encoding="utf-8") as f:
            for name in sorted(missing):
                f.write(json.dumps({
                    "type": "governance",
                    "name": "OMISSION_DETECTED",
                    "expected": name,
                    "ts": datetime.utcnow().isoformat() + "Z"
                }) + "\n")


def human_decision(decision, rationale):
    """Write a HUMAN_DECISION governance event."""
    event = {
        "type": "governance",
        "name": "HUMAN_DECISION",
        "decision": decision,
        "rationale": rationale,
        "ts": datetime.utcnow().isoformat() + "Z"
    }
    with open(_EVENTS_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")
