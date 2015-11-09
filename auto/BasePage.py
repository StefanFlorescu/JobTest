__author__ = 'Steve'

from auto.Instance import set_instance
from auto.AbstractPage import AbstractPage


class BasePage(AbstractPage):
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

def main_page(instance):
    return BasePage(instance)
if __name__ == '__main__':
    browser = set_instance()
    x = main_page(browser)
    x.login("testinginbox1@gmail.com", "test")
    x.wait()
    x.get_url("http://front.jobularity.com/zumay/")
