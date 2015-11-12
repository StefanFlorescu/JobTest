__author__ = 'LENOVO4'

from os import getcwd
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import csv
import time


class AbstractPage(object):
    def __init__(self, instance):
        assert isinstance(instance, (webdriver.Firefox, webdriver.Chrome, webdriver.Ie))
        self.driver = instance

    @staticmethod
    def wait(period=5):
        time.sleep(period)

    def get_url(self, url):
        assert "http" in url
        return self.driver.get(url)

    # pauses test execution until specified element is visible on the page
    def wait_until(self, locator, timeout= 60):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        except TimeoutException:
            print "the expected element is not visible, timeout exception raised, check for bugs"
            raise TimeoutException

    # returns True if element is on the page, else False is returned
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        else:
            return True

    # return True if element is visible within 2 seconds, otherwise False
    def is_element_visible(self, locator, timeout=2):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # return True if element is not visible within 3 seconds, otherwise False
    def is_not_visible(self, locator, timeout=2):
        try:
            ui.WebDriverWait(self.driver, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    # return True if element is clickable within 2 seconds, otherwise False
    def is_element_clickable(self, locator, timeout=2):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            return True
        except TimeoutException:
            return False

    def select_by_text(self, find_method, identifier, text):
        select = self.driver.find_element(by=find_method, value=identifier)
        select.find_element_by_xpath('//a[@class="ui-select-choices-row-inner"]/div[contains(text(),"%s")]'
                                     %text.strip()).click()

    def set_date(self, date="01/May/2010"):
        raw_date = date.split("/")
        day = raw_date[0]
        month = raw_date[1]
        year = raw_date[2]
        date_container = self.driver.find_element_by_xpath('//ul[@ng-model="date"]')
        toggle = date_container.find_element_by_xpath(
            '//button[@ng-click="toggleMode()"]/descendant::strong[@class="ng-binding"]')
        toggle.click()
        self.wait(1)
        toggle.click()
        self.wait(1)
        date_container.find_element_by_xpath(
            '//tbody/descendant::button[@type="button"]/span[contains(text(),%d)]'%year).click()
        date_container.find_element_by_xpath(
                    '//tbody/descendant::button[@type="button"]/span[contains(text(),%s)]'%month).click()
        date_container.find_element_by_xpath(
            '//tbody/descendant::button[@type="button"]/span[contains(text(),%s)]'%day).click()






if __name__ == '__main__':
    pass
