from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import yaml


@dataclass(frozen=True)
class Paths:
    root: Path
    workbench: Path
    vault: Path
    contests: Path

def _expand(value: str) -> Path:
    return Path(os.path.expandvars(os.path.expanduser(value))).resolve()

def load_config(path: str | Path | None = None) -> dict:
    if path is None:
        path = Path(__file__).resolve().parents[2] / 'config' / 'defaults.yaml'
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def resolve_paths(config: dict) -> Paths:
    p = config['paths']
    root = _expand(os.getenv('CUMMCM_ROOT', p['root']))
    return Paths(
        root=root,
        workbench=_expand(os.getenv('CUMMCM_WORKBENCH', p['workbench'])),
        vault=_expand(os.getenv('CUMMCM_VAULT', p['vault'])),
        contests=_expand(os.getenv('CUMMCM_CONTESTS', p['contests'])),
    )
