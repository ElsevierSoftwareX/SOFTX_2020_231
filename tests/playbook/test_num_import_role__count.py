import pytest
from io import StringIO
from ansiblemetrics.playbook.num_import_role import NumImportRole

#script_import
script_0 = "- name: Run tasks/other.yaml instead of 'main'\n- name: Pass variables to role\n- name: Apply condition to each task in role"
script_4 = "- import_role:\n\t\tname: myrole\n\n- name: Run tasks/other.yaml instead of 'main'\n\timport_role:\n\t\tname: myrole\n\t\ttasks_from: other\n\n- name: Pass variables to role\n\timport_role:\n\t\tname: myrole\n\tvars:\n\t\trolevar1: value from task\n\n- name: Apply condition to each task in role\n\timport_role:\n\t\tname: myrole\n\twhen: not idontwanttorun"

TEST_DATA = [
    (script_0, 0),
    (script_4, 4)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumImportRole(script).count()
    script.close()
    assert count == expected