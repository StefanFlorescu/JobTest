__author__ = 'LENOVO4'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time


class BasePage(object):
    def __init__(self, instance):
        assert isinstance(instance, (webdriver.Firefox, webdriver.Chrome, webdriver.Ie))
        self.driver = instance

    @staticmethod
    def wait(period=5):
        time.sleep(period)

    def select_by_text(self, find_method, id, text):
        select = Select(self.driver.find_element(by=find_method, value=id))
        select.select_by_visible_text(text)

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

    def register(self, user):
        driver = self.driver
        driver.find_element_by_link_text("Register Now").click()
        driver.find_element_by_name("firstName").send_keys(user.name)
        driver.find_element_by_name("lastName").send_keys(user.surename)
        driver.find_element_by_name("email").send_keys(user.email)
        driver.find_element_by_name("password").send_keys(user.password)
        driver.find_element_by_name("confirmPassword").send_keys(user.password)

        if user.role == "employer":
            driver.find_element_by_xpath(
                '//label[ng-class="{active: user.accountType == \'%s\'}"]' % (user.role)).click()
            driver.find_element_by_xpath('//input[@placeholder="Enter an industry..."]').click()
            self.select_by_text("xpath", '//ul/li[@class="ui-select-choices-group"]', "Banking")


if __name__ == '__main__':
    pass
