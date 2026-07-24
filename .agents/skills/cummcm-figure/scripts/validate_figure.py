from __future__ import annotations
from pathlib import Path
import argparse, ast, json, re

BAD_CMAPS={'jet','rainbow','gist_rainbow','nipy_spectral'}

def validate(path: Path) -> dict:
    text=path.read_text(encoding='utf-8'); findings=[]
    try: tree=ast.parse(text)
    except SyntaxError as e: return {'status':'FAIL','findings':[{'level':'FAIL','message':str(e)}]}
    if 'savefig' not in text: findings.append({'level':'WARN','message':'No savefig/export call detected'})
    if '.svg' not in text: findings.append({'level':'WARN','message':'No SVG export detected'})
    if '.pdf' not in text: findings.append({'level':'WARN','message':'No PDF export detected'})
    if '.png' not in text: findings.append({'level':'WARN','message':'No PNG preview export detected'})
    if 'svg.fonttype' not in text and 'apply_cummcm_style' not in text: findings.append({'level':'WARN','message':'Editable SVG text setting not detected'})
    for cmap in BAD_CMAPS:
        if re.search(rf"['\"]{re.escape(cmap)}['\"]",text): findings.append({'level':'FAIL','message':f'Unsafe rainbow colormap: {cmap}'})
    if re.search(r'\.sample\s*\(',text) and 'random_state' not in text: findings.append({'level':'FAIL','message':'Sampling without a recorded random_state'})
    if 'dropna(' in text and 'before_count' not in text and 'exclusion' not in text: findings.append({'level':'WARN','message':'dropna detected without explicit exclusion accounting'})
    level='FAIL' if any(x['level']=='FAIL' for x in findings) else ('WARN' if findings else 'PASS')
    return {'file':str(path),'status':level,'findings':findings}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('source'); ap.add_argument('--json',action='store_true'); ap.add_argument('--strict',action='store_true'); a=ap.parse_args()
    r=validate(Path(a.source)); print(json.dumps(r,ensure_ascii=False,indent=2) if a.json else f"{r['status']}: {len(r['findings'])} findings\n"+'\n'.join(f"- {x['level']}: {x['message']}" for x in r['findings']))
    raise SystemExit(1 if r['status']=='FAIL' or (a.strict and r['status']=='WARN') else 0)
if __name__=='__main__':main()
