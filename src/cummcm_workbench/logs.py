from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path


def append_log(path: str | Path, heading: str, fields: dict, quote: str | None=None) -> None:
    p=Path(path); p.parent.mkdir(parents=True,exist_ok=True)
    if not p.exists(): p.write_text(f'# {heading}\n\n',encoding='utf-8')
    lines=[f"## {datetime.now(UTC).isoformat()}",""]
    for k,v in fields.items(): lines.append(f"- **{k}：** {v}")
    if quote: lines.extend(['',f'> {quote.strip()}'])
    lines.append('')
    with p.open('a',encoding='utf-8') as f:f.write('\n'.join(lines)+'\n')
