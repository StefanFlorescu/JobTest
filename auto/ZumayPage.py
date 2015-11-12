__author__ = 'Steve'

from auto.BasePage import BasePage
from auto.Instance import set_instance

class Zumay(BasePage):

    def __init__(self, instance):
        super(BasePage, self).__init__(instance)

    def set_work(self):
        # ng-model="date"
        self.work_button.find_element_by_xpath('//i[@class="fa fa-plus-circle"]').click()
        work_container = self.driver.find_element_by_xpath('//div[@class="ngdialog-content"]')
        work_container.find_element_by_xpath('//i[@class="fa fa-calendar"]').click()
        self.set_date()


if __name__ == '__main__':
    x = set_instance()
    jobseeker = Zumay(x)
    jobseeker.login("testinginbox1@gmail.com", "test")
    jobseeker.wait()
    jobseeker.get_url("http://front.jobularity.com/zumay/")
    jobseeker.set_work()