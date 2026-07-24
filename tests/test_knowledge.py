from cummcm_workbench.knowledge import build_index, search


def test_index(tmp_path):
    (tmp_path/'x.md').write_text('---\ntitle: TOPSIS\nstatus: seeded\n---\n综合评价排序',encoding='utf-8')
    idx=tmp_path/'i.joblib'; build_index(tmp_path,idx)
    assert search(idx,'评价排序',1)[0]['title']=='TOPSIS'
