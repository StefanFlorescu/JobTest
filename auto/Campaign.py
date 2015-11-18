__author__ = 'Steve'
from auto.Instance import getcwd, get_dict

class JobCampaign(object):
    def __init__(self, entries):
        assert isinstance(entries, dict)
        self.__dict__.update(entries)

def set_job_campaign(dict_rep):
    dict_rep = get_dict(file_name, user_name)
    for key in dict_rep:
        if "dict" in dict_rep[key] or "{" in dict_rep[key]:
            dict_rep[key] = eval(dict_rep[key])
    return DictToObject(dict_rep)