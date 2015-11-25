__author__ = 'Steve'

import csv
from selenium import webdriver
from os import getcwd

jobseekers_csv = "demo_jobseekers.csv"
campaigns_csv = "demo_jobcampains.csv"


def work_dir():
    working_directory = getcwd()
    if working_directory.endswith("auto"):
        working_directory = working_directory[:-4] + "utils/"
    if working_directory.endswith("tests"):
        working_directory = working_directory[:-5] + "utils/"
    return working_directory

def dict_iterator(csv_file=jobseekers_csv):
    csvfile = open(work_dir() + csv_file)
    reader = csv.DictReader(csvfile)
    return reader

def get_dict(csv_file=jobseekers_csv, user_key="Robert"):
    try:
        with open(work_dir() + csv_file) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if user_key == row["name"]:
                    return row
    except IOError as (errno, strerror):
        print("I/O error({0}): {1}".format(errno, strerror))
    else:
        raise

class DictToObject(object):
    def __init__(self, dict_rep):
        assert isinstance(dict_rep, dict)
        for key in dict_rep:
            if "dict(" in dict_rep[key] or "{" in dict_rep[key]:
                dict_rep[key] = eval(dict_rep[key])
        self.__dict__.update(dict_rep)

def get_object_form_csv(file_name=jobseekers_csv, user_name="Robert"):
    dict_rep = get_dict(file_name, user_name)
    return DictToObject(dict_rep)

def get_object(dict_rep):
    return DictToObject(dict_rep)


def set_instance(browser_type="firefox", url_str="http://front.jobularity.com"):
    if browser_type.lower() in "opera":
        browser = webdriver.Opera("test string")
    elif browser_type.lower() in "google chrome":
        browser = webdriver.Chrome(work_dir() + "chromedriver.exe")
    elif browser_type.lower() in "internet explorer" or browser_type in "ie":
        browser = webdriver.Ie(work_dir() + "IEDriverServer.exe")
    else:
        browser = webdriver.Firefox()
    browser.get(url_str)
    browser.implicitly_wait(7)
    return browser

if __name__ == '__main__':
    print work_dir()
    # x = set_instance()
    # print type(x)
    # y = set_instance("chrome")
    # print type(y)
    # z = set_instance("ie")
    # print type(z)
    # csv_file = work_dir() + ""
    # csv_to_dict(csv_file)
    print get_object_form_csv("demo_jobseekers.csv", "Robert").__dict__
    with open(work_dir() + "demo_jobseekers.csv") as csvfile:
                reader = csv.DictReader(csvfile)
                print type(reader)

    print dict_iterator()
