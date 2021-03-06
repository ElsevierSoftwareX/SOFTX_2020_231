import pytest
from io import StringIO
from ansiblemetrics.playbook.num_ignore_errors import NumIgnoreErrors

#script_ignore_errors
script_0_1 = '- name: This command will change the working directory to somedir/ and will only run when somedir/somelog.txt does not exist.\n\tshell: somescript.sh >> somelog.txt\n\ttargs:\n\t\tchdir: somedir/\n\t\tpcreates: somelog.txt'
script_0_2 = '---\n-\n# NOTE (leseb): wait for mon discovery and quorum resolution\n# the admin key is not instantaneously created so we have to wait a bit\n- name: "wait for {{ cluster }}.client.admin.keyring exists"\n\twait_for:\n\t\tpath: /etc/ceph/{{ cluster }}.client.admin.keyring\n\twhen: cephx'
script_2 = '- name: Install, configure, and start Apache\n\tblock:\n\t- name: start service bar and enable it\n\t\tservice:\n\t\tname: bar\n\t\tstate: started\n\t\tenabled: True\n\twhen: ansible_facts[\'distribution\'] == \'CentOS\'\n\tignore_errors: yes\n- name: Attempt and graceful roll back demo\n\tblock:\n\t- debug:\n\t\tmsg: \'I execute normally\'\n\t- name: i force a failure\n\t\tcommand: /bin/false\n\t- debug:\n\t\tmsg: \'I never execute, due to the above task failing, :-(\'\n\tignore_errors: yes'

TEST_DATA = [
    (script_0_1, 0),
    (script_0_2, 0),
    (script_2, 2)
]

@pytest.mark.parametrize('script, expected', TEST_DATA)
def test(script, expected):
    script = StringIO(script.expandtabs(2))
    count = NumIgnoreErrors(script).count()
    script.close()
    assert count == expected