__author__ = 'LENOVO4'

import unittest
from auto.Instance import set_instance
from auto.BasePage import BasePage


instance = set_instance()
test = BasePage(instance)
test.login("Rebeckdon.gmail.com@cainari.info", "qwerty123")
test.logout()