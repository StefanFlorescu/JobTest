__author__ = 'LENOVO4'

from selenium import webdriver
from os import getcwd

def work_dir():
    working_directory = getcwd()
    if working_directory.endswith("auto"):
        working_directory = working_directory[:-5]
    return working_directory

def set_instance(browser_type = "firefox", url_str="http://front.jobularity.com"):

    if browser_type.lower() in "mozilla firefox":
        browser = webdriver.Firefox()
    elif browser_type.lower() in "google chrome":
        browser = webdriver.Chrome(work_dir()+"/utils/chromedriver.exe")
    elif browser_type.lower() in "interner explorer" or browser_type in "ie":
        browser = webdriver.Ie(work_dir()+"/utils/IEDriverServer.exe")
    else:
        browser = webdriver.Opera()
    browser.get(url_str)
    browser.implicitly_wait(10)
    return browser


if __name__ == '__main__':
    print work_dir()
    x = set_instance()
    print type(x)
    y = set_instance("chrome")
    print type(y)
    z = set_instance("ie")
    print type(z)