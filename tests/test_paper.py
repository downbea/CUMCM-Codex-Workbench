from cummcm_workbench.paper import assemble_markdown

def test_assemble(tmp_path):
    (tmp_path/'part.md').write_text('SECTION',encoding='utf-8')
    (tmp_path/'main.md').write_text('A\n{{INCLUDE:part.md}}\nB',encoding='utf-8')
    assert assemble_markdown(tmp_path/'main.md')=='A\nSECTION\nB'
