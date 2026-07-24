from __future__ import annotations

import re
from pathlib import Path

import joblib
import numpy as np
import yaml
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import normalize

FRONT = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)

def parse_note(path: Path) -> dict:
    text=path.read_text(encoding='utf-8')
    m=FRONT.match(text); meta={}
    body=text
    if m:
        meta=yaml.safe_load(m.group(1)) or {}; body=text[m.end():]
    return {'path':str(path),'relative_path':path.as_posix(),'metadata':meta,'body':body,'text':text}

def collect_notes(vault: str | Path, statuses=('approved','seeded')) -> list[dict]:
    vault=Path(vault); docs=[]
    for p in vault.rglob('*.md'):
        if '.obsidian' in p.parts: continue
        d=parse_note(p); status=str(d['metadata'].get('status',''))
        if status in statuses:
            d['relative_path']=p.relative_to(vault).as_posix(); docs.append(d)
    return docs

def build_index(vault: str | Path, output: str | Path) -> dict:
    docs=collect_notes(vault)
    corpus=[f"{d['metadata'].get('title','')} {' '.join(map(str,d['metadata'].get('aliases',[]) or []))} {d['body']}" for d in docs]
    word=TfidfVectorizer(ngram_range=(1,2),max_features=60000)
    char=TfidfVectorizer(analyzer='char_wb',ngram_range=(2,5),max_features=80000)
    wm=normalize(word.fit_transform(corpus)); cm=normalize(char.fit_transform(corpus))
    out=Path(output); out.parent.mkdir(parents=True,exist_ok=True)
    joblib.dump({'docs':docs,'word':word,'char':char,'wm':wm,'cm':cm},out)
    return {'documents':len(docs),'output':str(out)}

def search(index: str | Path, query: str, top_k=10) -> list[dict]:
    idx=joblib.load(index)
    qw=normalize(idx['word'].transform([query])); qc=normalize(idx['char'].transform([query]))
    scores=(idx['wm']@qw.T).toarray().ravel()*.25+(idx['cm']@qc.T).toarray().ravel()*.75
    order=np.argsort(-scores)[:top_k]; results=[]
    for i in order:
        d=idx['docs'][int(i)]
        results.append({'score':float(scores[i]),'path':d['relative_path'],'title':d['metadata'].get('title',Path(d['relative_path']).stem),'tier':d['metadata'].get('tier'),'category':d['metadata'].get('category')})
    return results
