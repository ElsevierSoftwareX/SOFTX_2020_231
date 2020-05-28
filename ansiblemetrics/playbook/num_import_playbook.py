import ansiblemetrics.utils as utils
from ansiblemetrics.ansible_metric import AnsibleMetric


class NumImportPlaybook(AnsibleMetric):
    """ This class implements the metric 'Number of import_playbook' in an Ansible script. """

    def count(self):
        script = self.playbook
        keys = utils.all_keys(script)
        return sum(1 for i in keys if i == 'import_playbook')
