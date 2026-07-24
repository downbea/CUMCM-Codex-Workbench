from __future__ import annotations
import argparse, json
from pathlib import Path
from .config import load_config, resolve_paths
from .contest import create_contest
from .manifest import write_manifest
from .data_audit import audit_file
from .knowledge import build_index, search
from .state import load_state, save_state, set_gate
from .audit import audit_markdown
from .freeze import freeze_artifacts
from .ocr import extract_pdf_text
from .paper import assemble_markdown

def main() -> None:
    parser=argparse.ArgumentParser(prog='cummcm')
    sub=parser.add_subparsers(dest='cmd',required=True)
    p=sub.add_parser('create-contest'); p.add_argument('--year',type=int,required=True); p.add_argument('--problem',required=True); p.add_argument('--force',action='store_true')
    p=sub.add_parser('manifest'); p.add_argument('root'); p.add_argument('--json',default='contest_manifest.json'); p.add_argument('--md',default='contest_manifest.md')
    p=sub.add_parser('audit-data'); p.add_argument('file'); p.add_argument('--output')
    p=sub.add_parser('build-index'); p.add_argument('--vault'); p.add_argument('--output')
    p=sub.add_parser('search'); p.add_argument('query'); p.add_argument('--index'); p.add_argument('--top-k',type=int,default=10)
    p=sub.add_parser('gate'); p.add_argument('state'); p.add_argument('gate'); p.add_argument('status'); p.add_argument('--note',default='')
    p=sub.add_parser('audit-paper'); p.add_argument('markdown')
    p=sub.add_parser('freeze'); p.add_argument('destination'); p.add_argument('files',nargs='+'); p.add_argument('--metadata',default='{}')
    p=sub.add_parser('extract-pdf'); p.add_argument('pdf'); p.add_argument('output_dir')
    p=sub.add_parser('assemble-paper'); p.add_argument('source'); p.add_argument('output')
    args=parser.parse_args(); cfg=load_config(); paths=resolve_paths(cfg)
    if args.cmd=='create-contest':
        template=Path(__file__).resolve().parents[2]/'templates'/'contest-project'
        print(create_contest(paths.contests,template,args.year,args.problem,args.force))
    elif args.cmd=='manifest': write_manifest(args.root,args.json,args.md); print(args.json,args.md)
    elif args.cmd=='audit-data': print(json.dumps(audit_file(args.file,args.output),ensure_ascii=False,indent=2))
    elif args.cmd=='build-index':
        vault=Path(args.vault or paths.vault); output=Path(args.output or vault/'99-System'/'index'/'knowledge.joblib')
        print(json.dumps(build_index(vault,output),ensure_ascii=False,indent=2))
    elif args.cmd=='search':
        idx=Path(args.index or paths.vault/'99-System'/'index'/'knowledge.joblib')
        print(json.dumps(search(idx,args.query,args.top_k),ensure_ascii=False,indent=2))
    elif args.cmd=='gate':
        s=load_state(args.state); set_gate(s,args.gate,args.status,args.note); save_state(args.state,s); print(json.dumps(s['gates'],ensure_ascii=False,indent=2))
    elif args.cmd=='audit-paper': print(json.dumps(audit_markdown(args.markdown),ensure_ascii=False,indent=2))
    elif args.cmd=='freeze': print(json.dumps(freeze_artifacts(args.files,args.destination,json.loads(args.metadata)),ensure_ascii=False,indent=2))
    elif args.cmd=='extract-pdf': print(json.dumps(extract_pdf_text(args.pdf,args.output_dir),ensure_ascii=False,indent=2))
    elif args.cmd=='assemble-paper': assemble_markdown(args.source,args.output); print(args.output)

if __name__=='__main__': main()
