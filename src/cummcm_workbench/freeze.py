from __future__ import annotations

import json
import shutil
from datetime import UTC, datetime
from pathlib import Path

from .hashing import sha256_file, stable_hash


def freeze_artifacts(paths: list[str | Path], destination: str | Path, metadata: dict) -> dict:
    dest=Path(destination); dest.mkdir(parents=True,exist_ok=True); records=[]
    for item in paths:
        src=Path(item)
        if not src.is_file(): raise FileNotFoundError(src)
        dst=dest/src.name
        if dst.exists(): raise FileExistsError(f'Refusing to overwrite frozen artifact: {dst}')
        shutil.copy2(src,dst); records.append({'name':dst.name,'sha256':sha256_file(dst),'source':str(src)})
    manifest={'frozen_at':datetime.now(UTC).isoformat(),'metadata':metadata,'artifacts':records}
    manifest['freeze_id']=stable_hash(manifest)[:16]
    (dest/'frozen_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    return manifest
