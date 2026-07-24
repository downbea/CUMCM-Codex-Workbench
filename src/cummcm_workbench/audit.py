from __future__ import annotations
from pathlib import Path
import json, re

SEVERITY_ORDER={'PASS':0,'MINOR':1,'MAJOR':2,'BLOCKER':3}

def audit_markdown(path: str | Path) -> dict:
    text=Path(path).read_text(encoding='utf-8')
    findings=[]
    for token in ['待补充','TODO','TBD','{{','[[STALE]]']:
        for m in re.finditer(re.escape(token),text):
            findings.append({'severity':'MAJOR' if token in {'待补充','TODO','TBD','[[STALE]]'} else 'MINOR','message':f'Unresolved marker: {token}','offset':m.start()})
    if '摘要' not in text: findings.append({'severity':'BLOCKER','message':'Missing abstract section'})
    if '参考文献' not in text: findings.append({'severity':'MAJOR','message':'Missing references section'})
    level=max((SEVERITY_ORDER[x['severity']] for x in findings),default=0)
    status={v:k for k,v in SEVERITY_ORDER.items()}[level]
    return {'file':str(path),'status':status,'findings':findings}
