from cummcm_workbench.dependency import affected_nodes


def test_affected():
    graph={'clean':['raw'],'model':['clean'],'figure':['model'],'paper':['figure','model']}
    assert affected_nodes(graph,['clean'])==['figure','model','paper']
