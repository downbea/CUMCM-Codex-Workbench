from __future__ import annotations
from pathlib import Path
import json, pandas as pd, numpy as np

def read_table(path: Path) -> dict[str, pd.DataFrame]:
    s=path.suffix.lower()
    if s in {'.xlsx','.xls'}:
        book=pd.ExcelFile(path)
        return {name:pd.read_excel(path,sheet_name=name) for name in book.sheet_names}
    if s=='.csv': return {'data':pd.read_csv(path)}
    if s in {'.tsv','.txt'}: return {'data':pd.read_csv(path,sep=None,engine='python')}
    raise ValueError(f'Unsupported table: {path}')

def audit_frame(df: pd.DataFrame) -> dict:
    numeric=df.select_dtypes(include=np.number)
    duplicates=int(df.duplicated().sum())
    outliers={}
    for c in numeric.columns:
        q1,q3=numeric[c].quantile([.25,.75]); iqr=q3-q1
        outliers[str(c)]=int(((numeric[c] < q1-1.5*iqr)|(numeric[c] > q3+1.5*iqr)).sum()) if pd.notna(iqr) else 0
    return {
        'rows':int(df.shape[0]),'columns':int(df.shape[1]),'duplicate_rows':duplicates,
        'missing':{str(k):int(v) for k,v in df.isna().sum().items()},
        'dtypes':{str(k):str(v) for k,v in df.dtypes.items()},'iqr_outlier_counts':outliers,
        'numeric_summary':numeric.describe().round(6).to_dict() if not numeric.empty else {}
    }

def audit_file(path: str | Path, output: str | Path | None=None) -> dict:
    path=Path(path); result={'file':str(path),'sheets':{}}
    for name,df in read_table(path).items(): result['sheets'][name]=audit_frame(df)
    if output: Path(output).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
    return result
