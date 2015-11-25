__author__ = 'Steve'

from auto.AbstractPage import AbstractPage
from auto.Instance import set_instance, get_object_form_csv
from auto.BasePage import enter_page

class ZumayPage(AbstractPage):
    def __init__(self, browser):
        AbstractPage.__init__(self, browser)
        if "/zumay/" not in self.driver.current_url:
            self.driver.get("http://front.jobularity.com/zumay/")

    def set_language(self, user_object):
        for language in user_object.languages:
            language_container = self.driver.find_element_by_xpath('//div[@zumay-languages=""]')
            language_container.find_element_by_xpath('div/div[1]/div/div/ul/li[2]').click()
            popup = self.driver.find_element_by_xpath('//body/div[2]/div[@class="ngdialog-content" and@role="document"]')
            assert "Languages" == popup.find_element_by_tag_name("h2").get_attribute('textContent')
            self.select_dropdown_text(popup, '//span[@ng-click="$select.activate()"]', language['value'])
            self.select_option_text(popup, '//select[@ng-model="item.proficiency"]', language["proficiency"])
            popup.find_element_by_xpath('//button[text()="Add to Zumay"]').click()
            self.is_not_visible('//div[@class="ngdialog-content" and@role="document"]')



    def set_skills(self, user_object):
        for skill in user_object.skills:
            skills_container = self.driver.find_element_by_xpath('//div[@zumay-skills=""]')
            skills_container.find_element_by_xpath('div/div[2]/div[1]/div/div/ul/li[2]/a').click()
            popup = self.driver.find_element_by_xpath('//body/div[2]/div[@class="ngdialog-content" and@role="document"]')
            assert "Manage your Skill" == popup.find_element_by_tag_name("h2").get_attribute('textContent')
            if skill["isprimary"]:
                self.select_dropdown_text(popup, '//span[@ng-click="$select.activate()"]', skill['value'])
                popup.find_element_by_xpath('//input[@ng-model="item.isPrimary"]').click()
                self.wait(1)
                popup.find_element_by_xpath('//input[@ng-model="item.rank"]').send_keys(str(skill['rank']))
            else:
                self.select_dropdown_text(popup, '//span[@ng-click="$select.activate()"]', skill['value'])
            popup.find_element_by_xpath('//button[text()="Add to Zumay"]').click()
            if self.is_not_visible('//div[@class="ngdialog-content" and @role="document"]'):
                pass


    def set_education(self, user_object):
        for education in user_object.education:
            education_container = self.driver.find_element_by_xpath('//div[@zumay-skills=""]')
            education_container.find_element_by_xpath('div/div[2]/div[1]/div/div/ul/li[2]/a').click()
            popup = self.driver.find_element_by_xpath('//body/div[2]/div[@class="ngdialog-content" and@role="document"]')
            assert "Manage your Skill" == popup.find_element_by_tag_name("h2").get_attribute('textContent')
            if skill["isprimary"]:
                self.select_dropdown_text(popup, '//span[@ng-click="$select.activate()"]', education['value'])
                popup.find_element_by_xpath('//input[@ng-model="item.isPrimary"]').click()
                self.wait(1)
                popup.find_element_by_xpath('//input[@ng-model="item.rank"]').send_keys(str(education['rank']))
            else:
                self.select_dropdown_text(popup, '//span[@ng-click="$select.activate()"]', education['value'])
            popup.find_element_by_xpath('//button[text()="Add to Zumay"]').click()
            if self.is_not_visible('//div[@class="ngdialog-content" and @role="document"]'):
                pass

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
                driver.find_element_by_xpath(
                    '//div[@class="ngdialog-content"]/descendant::label[@ng-class="{active: answer == 1}"]').click()
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
    jobseeker = get_object_form_csv(user_name="Robert")
    enter = enter_page(browser)
    enter.login(jobseeker)
    profile = zumay_page(browser)
    # profile.set_language(jobseeker)
    # profile.set_skills(jobseeker)
    profile.set_education(jobseeker)
