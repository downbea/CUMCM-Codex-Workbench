from cummcm_workbench.state import new_state, set_gate


def test_gate():
    s=new_state(2026,'A')
    set_gate(s,'topic_selected','APPROVED','human confirmed')
    assert s['gates']['topic_selected']=='APPROVED'
