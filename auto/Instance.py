__author__ = 'LENOVO4'

from selenium import webdriver
from os import getcwd as work_dir


class Instance(object):

    def __init__(self, browser_type, url_str):

        if browser_type in "mozilla firefox":
            self.browser = webdriver.Firefox()
        elif browser_type in "google chrome":
            self.browser = webdriver.Chrome(work_dir()+"/utils/chromedriver.exe")
        elif browser_type in "interner explorer" or browser_type in "ie":
            self.browser = webdriver.Ie(work_dir()+"/utils/IEDriverServer.exe")
        # elif browser in "opera":
        #     self.browser = webdriver.Opera()
        self.browser.get(url_str)
        self.browser.implicitly_wait(10)

def set_instance(browser ="firefox", url ="http://front2.jobularity.com"):

    return Instance(browser, url).browser