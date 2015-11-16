__author__ = 'Steve'

from auto.AbstractPage import AbstractPage
from auto.Instance import set_instance, set_user
from auto.BasePage import enter_system

class ZumayPage(AbstractPage):
    # def __init__(self):
    #     super(AbstractPage, self).__init__()
    #     self.language_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'languages'"]''')
    #     self.skill_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'skills'"]''')
    #     self.education_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'education_certifications'"]''')
    #     self.experience_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'work_experience'"]''')
    #     self.profile_media = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'profile_media'"]''')
    #     self.bio_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'about_me'"]''')

    def set_language(self, user):
        language_container = self.driver.find_element_by_xpath('''//div[@class="fw"]/descendant::div[@ng-if="value === 'languages'"]''')
        language_container.find_element_by_xpath('//ul[@class="edit-list"]/li[@ng-click="addZumaySection()" and @class="ng-scope"]')\
            .click()
        # ng-model
        # self.work_button.find_element_by_xpath('//i[@class="fa fa-plus-circle"]').click()
        # work_container = self.driver.find_element_by_xpath('//div[@class="ngdialog-content"]')
        # work_container.find_element_by_xpath('//i[@class="fa fa-calendar"]').click()
        # self.set_date()
def zumay(instance):
    return ZumayPage(instance)

if __name__ == '__main__':
    browser = set_instance()
    jobseeker = set_user(user_name="David")
    enter = enter_system(browser)
    enter.login(jobseeker)
    enter.wait()
    # enter.get_url("http://front.jobularity.com/zumay/")
    profile = zumay(browser)
    profile.set_language(jobseeker)