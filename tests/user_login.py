__author__ = 'LENOVO4'

import unittest
from auto.Instance import set_instance, set_user
from auto.BasePage import BasePage


if __name__ == '__main__':

    instance = set_instance()
    Dian = set_user("demo_jobseekers.csv", "Dian")
    test = BasePage(instance)
    test.login(Dian)
    # test.register(stephen)