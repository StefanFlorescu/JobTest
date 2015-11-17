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
        language_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'languages'"]''')
        language_container.find_element_by_xpath('''//ul[@class="edit-list"]/li[@ng-if="optionShown('add-new')"]/a''')\
            .click()
        print language_container.find_element_by_xpath('//h3/b').get_attribute("textContent")

    def set_skills(self, user):
        skills_container = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'skills'"]''')
        skills_container.find_element_by_xpath('''//ul[@class="edit-list"]/li[@ng-if="optionShown('add-new')"]/a/i''')\
            .click()

    def set_education(self, user):
        education_contaibner = self.driver.find_element_by_xpath('''//div[@ng-if="value === 'education'"]''')
        education_contaibner.find_element_by_xpath('''//ul[@class="edit-list"]/li[@ng-if="optionShown('add-new')"]/a/i''')\
            .click()
def zumay(instance):
    return ZumayPage(instance)

if __name__ == '__main__':
    browser = set_instance()
    jobseeker = set_user(user_name="David")
    enter = enter_system(browser)
    enter.login(jobseeker)
    # enter.wait()
    enter.get_url("http://front.jobularity.com/zumay/")
    profile = zumay(browser)
    profile.set_skills(jobseeker)
    # profile.set_language(jobseeker)