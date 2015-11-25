__author__ = 'Steve'

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
    def wait_until(self, xpath_locator, timeout= 60):
        try:
            ui.WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, xpath_locator)))
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

    def switch_window(self):
        self.wait(2)
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[1])
        print "have switched to %s window"%self.driver.title

    def switch_window_back(self):
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])
        self.wait(1)
        print "have switched to %s window"%self.driver.title

    @staticmethod
    def select_dropdown_text( container_object, click_element, match_text):
        container_object.find_element_by_xpath(click_element).click()
        container_object.find_element_by_xpath('//ul[@role="listbox"]/descendant::*[contains(text(),"%s")]'%match_text).click()

    @staticmethod
    def select_option_text(container_object, select_element, match_text):
        select = Select(container_object.find_element_by_xpath(select_element))
        select.select_by_visible_text(match_text)

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

    def logout(self):
        driver = self.driver
        driver.find_element_by_class_name("user-img-x").click()
        driver.find_element_by_link_text("Log out").click()

    def close(self):
        self.driver.close()



if __name__ == '__main__':
    pass
