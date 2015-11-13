__author__ = 'Steve'

import unittest
from auto.Instance import set_instance, set_user
from auto.BasePage import BasePage


if __name__ == '__main__':

    instance = set_instance()
    jobseeker = set_user("demo_jobseekers.csv", "Jeefrey")
    test = BasePage(instance)
    # test.login(jobseeker)
    test.wait()
    test.register(jobseeker)