from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json

DEFAULT_GATES = {
    'topic_selected': 'PENDING',
    'cleaning_approved': 'PENDING',
    'model_approved': 'PENDING',
    'results_frozen': 'PENDING',
    'logic_audit': 'PENDING',
    'consistency_audit': 'PENDING',
    'compliance_audit': 'PENDING',
    'final_release': 'PENDING',
}

def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()

def new_state(year: int, problem: str) -> dict:
    pid = f'{year}-{problem.upper()}'
    return {
        'project_id': pid, 'year': year, 'problem': problem.upper(),
        'stage': 'CREATED', 'updated_at': utc_now(),
        'tasks': {}, 'gates': DEFAULT_GATES.copy(), 'artifacts': {},
        'stale': [], 'decisions': []
    }

def load_state(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding='utf-8'))

def save_state(path: str | Path, state: dict) -> None:
    state['updated_at'] = utc_now()
    p = Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + '.tmp')
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(p)

def set_gate(state: dict, gate: str, status: str, note: str = '') -> dict:
    if gate not in state['gates']: raise KeyError(gate)
    allowed = {'PENDING','APPROVED','REJECTED','STALE','BLOCKED','RISK_ACCEPTED'}
    if status not in allowed: raise ValueError(status)
    state['gates'][gate] = status
    state['decisions'].append({'time': utc_now(), 'gate': gate, 'status': status, 'note': note})
    return state

def mark_stale(state: dict, artifacts: list[str], reason: str) -> dict:
    for artifact in artifacts:
        state['stale'].append({'artifact': artifact, 'reason': reason, 'time': utc_now()})
    return state
