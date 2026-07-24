from __future__ import annotations
from pathlib import Path
import json

def extract_pdf_text(pdf: str | Path, output_dir: str | Path) -> dict:
    try: import fitz
    except ImportError as e: raise RuntimeError('Install OCR extras: pip install .[ocr]') from e
    pdf=Path(pdf); out=Path(output_dir); out.mkdir(parents=True,exist_ok=True)
    doc=fitz.open(pdf); pages=[]
    for i,page in enumerate(doc):
        text=page.get_text('text').strip(); mode='embedded_text'
        if len(text)<30:
            pix=page.get_pixmap(matrix=fitz.Matrix(2,2),alpha=False); image=out/f'page-{i+1}.png';pix.save(image); mode='needs_ocr';text=''
        pages.append({'page':i+1,'mode':mode,'text':text,'confidence':1.0 if mode=='embedded_text' else 0.0})
    (out/'extraction.json').write_text(json.dumps(pages,ensure_ascii=False,indent=2),encoding='utf-8')
    (out/'extracted.md').write_text('\n\n'.join(f"## 第 {p['page']} 页\n\n{p['text'] or '[需要 OCR 与人工校对]'}" for p in pages),encoding='utf-8')
    return {'pages':len(pages),'needs_ocr':sum(p['mode']=='needs_ocr' for p in pages)}
