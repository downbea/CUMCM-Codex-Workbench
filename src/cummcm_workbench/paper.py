from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

INCLUDE_RE=re.compile(r'\{\{INCLUDE:([^}]+)\}\}')

def assemble_markdown(source: str | Path, output: str | Path | None=None) -> str:
    source=Path(source); text=source.read_text(encoding='utf-8')
    seen={source.resolve()}
    def expand(base: Path, raw: str) -> str:
        def repl(m):
            child=(base/m.group(1).strip()).resolve()
            if child in seen: raise RuntimeError(f'Circular include: {child}')
            if not child.is_file(): raise FileNotFoundError(child)
            seen.add(child)
            child_text=child.read_text(encoding='utf-8')
            result=expand(child.parent,child_text)
            seen.remove(child)
            return result
        return INCLUDE_RE.sub(repl,raw)
    assembled=expand(source.parent,text)
    if output: Path(output).write_text(assembled,encoding='utf-8')
    return assembled

def build_docx(markdown: Path, output_docx: Path, reference_docx: Path, bibliography: Path | None=None, csl: Path | None=None) -> None:
    pandoc=shutil.which('pandoc')
    if not pandoc: raise RuntimeError('pandoc not found')
    assembled=output_docx.with_suffix('.assembled.md'); assemble_markdown(markdown,assembled)
    cmd=[pandoc,str(assembled),'--from','markdown+tex_math_dollars','--standalone','--toc','--reference-doc',str(reference_docx),'-o',str(output_docx)]
    if bibliography:
        cmd.extend(['--citeproc','--bibliography',str(bibliography)])
        if csl: cmd.extend(['--csl',str(csl)])
    subprocess.run(cmd,check=True)
