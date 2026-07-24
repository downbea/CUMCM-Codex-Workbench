from __future__ import annotations
from pathlib import Path
import shutil
from .state import new_state, save_state

def create_contest(root: Path, template: Path, year: int, problem: str, force: bool = False) -> Path:
    problem = problem.upper()
    target = root / str(year) / problem
    if target.exists() and any(target.iterdir()) and not force:
        raise FileExistsError(f'{target} already exists and is not empty')
    target.mkdir(parents=True, exist_ok=True)
    shutil.copytree(template, target, dirs_exist_ok=True)
    replacements = {'{{YEAR}}': str(year), '{{PROBLEM}}': problem, '{{PROJECT_ID}}': f'{year}-{problem}'}
    for p in target.rglob('*'):
        if p.is_file() and p.suffix.lower() in {'.md','.yaml','.yml','.json','.txt'}:
            try: text = p.read_text(encoding='utf-8')
            except UnicodeDecodeError: continue
            for a,b in replacements.items(): text = text.replace(a,b)
            p.write_text(text, encoding='utf-8')
    save_state(target/'project_state.json', new_state(year, problem))
    return target
