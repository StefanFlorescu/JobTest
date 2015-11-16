__author__ = 'Steve'

import unittest
from auto.Instance import set_instance, set_user
from auto.BasePage import BasePage


if __name__ == '__main__':

    instance = set_instance()
    jobseeker1 = set_user(user_name="Robert")
    test = BasePage(instance)
    test.login(jobseeker1)
    test.wait()
    test.logout()
    jobseeker2 = set_user(user_name="David")
    test.login(jobseeker2)
    test.wait()
    test.logout()
    jobseeker3 = set_user(user_name="Louisa")
    test.login(jobseeker3)
    test.wait()
    test.logout()
    jobseeker4 = set_user(user_name="Jeefrey")
    test.login(jobseeker4)
    test.wait()
    test.logout()
