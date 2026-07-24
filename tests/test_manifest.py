from cummcm_workbench.manifest import build_manifest

def test_manifest(tmp_path):
    (tmp_path/'a.txt').write_text('x',encoding='utf-8')
    m=build_manifest(tmp_path)
    assert len(m['files'])==1 and m['files'][0]['sha256']
