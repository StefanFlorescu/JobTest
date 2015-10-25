__author__ = 'LENOVO4'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class BasePage(object):
    
    def __init__(self, instance):
        assert isinstance(instance, (webdriver.Firefox, webdriver.Chrome, webdriver.Ie))
        self.driver = instance

    def login(self, email, password):
        driver = self.driver
        driver.find_element_by_css_selector("button.identif_butt").click()
        driver.find_element_by_name("usermail").send_keys(email)
        driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
        driver.find_element_by_css_selector("button.sign-in").click()

    def logout(self):
        driver = self.driver
        driver.find_element_by_class_name("user-img-x").click()
        driver.find_element_by_link_text("Log out").click()