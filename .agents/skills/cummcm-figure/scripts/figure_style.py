from __future__ import annotations
from pathlib import Path
import matplotlib as mpl
import matplotlib.pyplot as plt

FONT_CANDIDATES=['Microsoft YaHei','SimHei','Noto Sans CJK SC','DejaVu Sans']

def apply_cummcm_style() -> None:
    mpl.rcParams.update({
        'font.family':'sans-serif','font.sans-serif':FONT_CANDIDATES,
        'axes.unicode_minus':False,'axes.spines.top':False,'axes.spines.right':False,
        'figure.dpi':120,'savefig.dpi':300,'svg.fonttype':'none','pdf.fonttype':42,
        'axes.grid':False,'legend.frameon':False,'figure.facecolor':'white','axes.facecolor':'white'
    })

def export_figure(fig: plt.Figure, stem: str | Path, png_dpi: int=300) -> list[Path]:
    stem=Path(stem); stem.parent.mkdir(parents=True,exist_ok=True)
    outputs=[]
    for suffix,kwargs in [('.svg',{}),('.pdf',{}),('.png',{'dpi':png_dpi})]:
        p=stem.with_suffix(suffix); fig.savefig(p,bbox_inches='tight',facecolor='white',**kwargs); outputs.append(p)
    return outputs
