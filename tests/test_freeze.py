from cummcm_workbench.freeze import freeze_artifacts


def test_freeze(tmp_path):
    src=tmp_path/'x.json';src.write_text('{"x":1}',encoding='utf-8')
    m=freeze_artifacts([src],tmp_path/'frozen',{'seed':2026})
    assert m['artifacts'][0]['sha256'] and (tmp_path/'frozen/frozen_manifest.json').exists()
