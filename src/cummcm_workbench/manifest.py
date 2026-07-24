from __future__ import annotations
from pathlib import Path
from datetime import datetime, timezone
import json, mimetypes
from .hashing import sha256_file

def build_manifest(root: str | Path) -> dict:
    root = Path(root).resolve(); items=[]
    for p in sorted(root.rglob('*')):
        if not p.is_file() or '.git' in p.parts: continue
        stat=p.stat(); mime,_=mimetypes.guess_type(p.name)
        items.append({
            'path': p.relative_to(root).as_posix(), 'suffix': p.suffix.lower(),
            'size_bytes': stat.st_size, 'modified_utc': datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat(),
            'sha256': sha256_file(p), 'mime': mime or 'application/octet-stream'
        })
    return {'root': str(root), 'generated_at': datetime.now(timezone.utc).isoformat(), 'files': items}

def write_manifest(root: str | Path, json_path: str | Path, md_path: str | Path) -> None:
    data=build_manifest(root)
    Path(json_path).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    lines=['# 赛题文件清单','',f"生成时间：{data['generated_at']}",'','| 文件 | 类型 | 大小 | SHA-256 前 12 位 |','|---|---:|---:|---|']
    for x in data['files']:
        lines.append(f"| `{x['path']}` | `{x['suffix'] or 'none'}` | {x['size_bytes']} | `{x['sha256'][:12]}` |")
    Path(md_path).write_text('\n'.join(lines)+'\n',encoding='utf-8')
