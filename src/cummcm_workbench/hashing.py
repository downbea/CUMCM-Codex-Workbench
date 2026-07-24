from __future__ import annotations

import hashlib
import json
from pathlib import Path


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size): h.update(chunk)
    return h.hexdigest()

def stable_hash(data) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return hashlib.sha256(raw).hexdigest()
