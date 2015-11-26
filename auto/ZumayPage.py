__author__ = 'Steve'

from auto.AbstractPage import AbstractPage
from auto.Instance import set_instance, get_object_form_csv
from auto.BasePage import enter_page

class ZumayPage(AbstractPage):

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

class SearchPage(AbstractPage):

    def search_job(self, job):
        driver = self.driver
        driver.find_element_by_xpath("//a[@href='/search']").click()

        place = driver.find_element_by_xpath('//input[@ng-model="search.location"]')
        place.clear()
        place.send_keys(job.location)
        position = driver.find_element_by_xpath("//input[@ng-model='search.title']")
        position.clear()
        position.send_keys(job.name)
        self.wait(1)
        company = driver.find_element_by_xpath(
            '//jbt-job-search-filters/descendant::span[contains(text(),"%s")]/preceding-sibling::input'%job.company)
        company.click()
        self.wait(2)
        # self.wait_until('//div[@class="element-description"]/h4/a[contains(text(),"$s")]')
        driver.find_element_by_partial_link_text(job.name).click()

    def apply_to_job(self, job):
        driver = self.driver
        self.wait_until('//div[@class="sticky-apply ng-scope"]')
        if self.is_element_visible('//button[contains(text(),"Apply for this Job")]', 1):
            application = driver.find_element_by_xpath('//button[contains(text(),"Apply for this Job")]')
            application.click()
            if self.is_element_visible('//div[@class="ngdialog-content"]', 2):
                if job.answer.lower() == "yes":
                    driver.find_element_by_xpath(
                        '//div[@class="ngdialog-content"]/descendant::label[@ng-class="{active: answer == 1}"]').click()
                    driver.find_element_by_xpath(
                        '//div[@class="ngdialog-content"]/descendant::button[contains(text(),"Apply")]').click()
                else:
                    driver.find_element_by_xpath(
                        '//div[@class="ngdialog-content"]/descendant::label[@ng-class="{active: answer == 0}"]').click()
                    driver.find_element_by_xpath(
                        '//div[@class="ngdialog-content"]/descendant::button[contains(text(),"Apply")]').click()
            assert self.is_element_visible(
                '//jbt-jobseeker-dashboard-jobs/descendant::a[contains(text(),"%s")]/following-sibling::span[contains(text(),"%s")]'\
                %(job.name, job.location))
            print "have applied to the job campaign"
            self.wait(2)
        else:
            print "jobseeker has already applied to this job campaign"


def zumay_page(instance):
    return ZumayPage(instance)

def search_page(instance):
    return SearchPage(instance)

if __name__ == '__main__':
    browser = set_instance()
    jobseeker = get_object_form_csv(user_name="David")
    enter = enter_page(browser)
    enter.login(jobseeker)
    # enter.wait()
    enter.get_url("http://front.jobularity.com/zumay/")
    profile = zumay_page(browser)
    profile.set_skills(jobseeker)
    # profile.set_language(jobseeker)