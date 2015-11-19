
from os import getcwd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as EC
import selenium.webdriver.support.ui as ui
import csv
import time

# returns dictionary of the csv file inputed
def getdict(filename):

    with open(getcwd()+"/utils/"+filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        pool = dict()
        for row in reader:
            pool[row[0]]=list((row[1],row[2]))
        return pool

# returns the Firefox browser instance and loads the default page
def set_instance(url_rep):
    driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url_rep)
    return driver


# staticmethod that pauses the program execution for a defined time
def wait(pause=5):
    time.sleep(pause)

def wait_until(instance, locator, timeout = 60):
    try:
        ui.WebDriverWait(instance, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
    except TimeoutException:
        print "the expected element is not visible, timeout exception raised, check for bugs"
        raise TimeoutException

# returns True if the element is present on the page
def is_element_present(instance, how, what):
    try:
        instance.find_element(by=how, value=what)
    except NoSuchElementException:
        return False
    else:
        return True

# return True if element is visible within 2 seconds, otherwise False
def is_element_visible(instance, locator, timeout=10):
    try:
        ui.WebDriverWait(instance, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# return True if element is not visible within 3 seconds, otherwise False
def is_not_visible(instance, locator, timeout=10):
    try:
        ui.WebDriverWait(instance, timeout).until_not(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# return True if element is clickable within 2 seconds, otherwise False
def is_element_clickable(instance, locator, timeout=10):
    try:
        ui.WebDriverWait(instance, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
        return True
    except TimeoutException:
        return False

# returns True is the instance is a version of front
def is_front(instance):
    if "front" in instance.current_url:
        return True
    else:
        return False

# returns the str representation of the instance name
def instance_type(instance):
    if "front2" in instance.current_url:
        return "front2 instance"
    elif "front" in instance.current_url:
        return "front instance"
    else:
        return "dev instance"

# returns True if the user (jobseeker, employer) has its account uncompleted
def is_uncomplete(instance):
    if "wizard/welcome" in instance.current_url:
        print "this user has not completed his registration yet"
        return True
    elif "/account?pass-reset-token" in instance.current_url:
        print "this user has not completed his registration yet"
        return True
    elif "/start" in instance.current_url:
        print "this user has not completed his registration yet"
        return True
    else:
        return False






def login(instance, role, user_key, user_pass):
        driver = instance

        if is_front(instance):
            # user_key = user_key[:-13]
            # user_key = user_key + ".cainari.info@cainari.info"
            driver.find_element_by_css_selector("button.identif_butt").click()
            driver.find_element_by_name("usermail").send_keys(user_key)
            driver.find_element_by_xpath("//input[@name='password']").send_keys(user_pass)
            driver.find_element_by_css_selector("button.sign-in").click()
            assert is_element_present(instance, "id", "page_header")
        else:
            driver.find_element_by_link_text("Sign in").click()
            driver.find_element_by_name("name").send_keys(user_key)
            driver.find_element_by_xpath("//input[@name='pass']").send_keys("test1")
            driver.find_element_by_name("op").click()
            assert is_element_present(instance, "xpath", '//div[@class="header page-region"]')
        print "have entered the system as {0} ( email {1} || password {2}) on the '{3}' ".format(role, user_key, user_pass, instance_type(instance))
        # wait(2)

def logout(instance):
        driver = instance
        if is_front(instance):
            menu = driver.find_element_by_xpath('//ul[@class="right_top_menu"]/li[@class="dropdown user-drop"]')
            menu.find_element_by_xpath('//i[@class="fa fa-caret-down"]').click()
            menu.find_element_by_xpath('//a[@ng-click="authService.logout()"]').click()
        else:
            driver.find_element_by_class_name("full-name").click()
            driver.find_element_by_xpath("Log out").click()

def get_employer_info(instance):
        data = list()
        driver = instance

        if is_uncomplete(instance):
            return data
        else:
            if is_front(driver):

                driver.find_element_by_css_selector("i.fa.fa-caret-down").click()
                driver.find_element_by_link_text("Personal Profile").click()
                wait()
                x = driver.find_element_by_name("firstName").get_attribute("value")
                y = driver.find_element_by_name("lastName").get_attribute("value")
                z = driver.find_element_by_xpath("//select[@id='country']/option[@selected='selected']").get_attribute("innerText")
                print "{0} {1} at address {2}".format(x, y, z)

                for i in (x, y, z):
                    data.append(i)
                return data
            else:

                driver.find_element_by_id("small_menu_userpic").click()
                driver.find_element_by_link_text("My account").click()
                wait()
                x = driver.find_element_by_id("edit-field-first-name-und-0-value").get_attribute("value")
                y = driver.find_element_by_id("edit-field-last-name-und-0-value").get_attribute("value")
                driver.get("https://dev.jobularity.com/plugins/addressbook")
                z = driver.find_element_by_xpath('//div[@class="b-box alert-grey fw pad15 f-size-12"]').get_attribute("innerText")
                print "{0} {1} at address {2}".format(x, y, z)

                for i in (x, y, z):
                    data.append(i)
                return data

def get_jobseeker_info(instance):
        driver = instance
        data = list()

        if is_uncomplete(instance):
            return data
        else:

            if is_front(instance):
                driver.find_element_by_css_selector("i.fa.fa-caret-down").click()
                driver.find_element_by_link_text("Personal Profile").click()
                wait()
                x = driver.find_element_by_name("firstName").get_attribute("value")
                y = driver.find_element_by_name("lastName").get_attribute("value")
                z = driver.find_element_by_xpath('//input[@id="email"]').get_attribute("value")
                print "{0} {1} at email address {2}".format(x,y,z)
                for i in (x,y,z):
                    data.append(i.strip())

                return data
            else:

                driver.find_element_by_id("small_menu_userpic").click()
                driver.find_element_by_link_text("My account").click()
                wait()
                x = driver.find_element_by_id("edit-field-first-name-und-0-value").get_attribute("value")
                y = driver.find_element_by_id("edit-field-last-name-und-0-value").get_attribute("value")
                z = driver.find_element_by_id("edit-mail").get_attribute("value")
                print "{0} {1} at email address {2}".format(x,y,z)
                for i in (x,y,z):
                    data.append(i.strip())

                return data

def get_addresses(instance):
    driver = instance
    address = []

    if is_uncomplete(instance):
        return address
    else:

        if is_front(instance):

            driver.get("http://front2.jobularity.com/employer/preferences/offices")
            wait()
            address_pool = driver.find_elements_by_xpath('//div[@class="office"]/descendant::span[@class="label ng-binding"]')

        else:
            driver.get("http://dev.jobularity.com/plugins/addressbook")
            wait()
            address_pool = driver.find_elements_by_xpath('//div[@class="fw address-book-ino"]/descendant::div[@class="b-box alert-grey fw pad15 f-size-12"]')

        for i in address_pool:
            address.append(i.get_attribute("textContent").strip(" "))
        address.sort()
        print "this  user has {0} addresses".format(len(address))
        print address
        return address

def get_videos(instance):
    driver = instance
    data = 0

    if is_uncomplete(instance):
        return data

    else:

        if is_front(instance):
            driver.get("http://front2.jobularity.com/employer/videos")
            videos = driver.find_elements_by_xpath('//div[@class="videos-list col-xs-7"]/descendant::span[@ng-if="video.video_name"]')
            data = len(videos)
        else:
            driver.get("https://dev.jobularity.com/node/add/job-opportunity")
            driver.find_element_by_xpath('//strong[contains(text(),"Videos")]').click()
            driver.find_element_by_xpath('//span[@class="add-video-options"]').click()
            driver.find_element_by_xpath('//input[@value="Add from library"]').click()
            video_popup = driver.find_element_by_xpath('//div[@class="jobularity-popup-header"]')
            videos = video_popup.find_elements_by_xpath('//div[@class="video-data col-xs-9"]')
            video_popup.find_element_by_xpath('//span[@class="jobularity-popup-header-close"]').click()
            wait(1)
            data = len(videos)
    print "this user has {0} videos in his account".format(data)
    return data

def get_questions(instance):
    driver = instance
    data = []

    if is_uncomplete(instance):
        return data
    else:

        if is_front(instance):
            driver.get("http://front2.jobularity.com/employer/questions")
            question_pool = len(driver.find_elements_by_xpath(
                '//div[@class="questions-list col-xs-6"]/div[@class="fw"]/jbt-question-library-rows'))
            for item in xrange(1, question_pool+1):
                text = driver.find_element_by_xpath(
                    '//jbt-question-library-rows[%d]/descendant::div[@class="pad-r-30"]/p[@class="text t-def ng-binding"]'%item)\
                    .get_attribute("textContent")
                data.append(text.strip())
        else:
            driver.get("https://dev.jobularity.com/library")
            categories = driver.find_elements_by_xpath('//div[@class="box-bdy pad15 fw"]/descendant::span[@class="title"]')

            for option in categories:
                option.click()
                question_pool = driver.find_elements_by_xpath('//div[@id="questions-list-lib"]/ul/li/p')
                for item in question_pool:

                    try:
                        text = item.get_attribute("textContent")
                    except :
                        pass
                    else:
                        data.append(text.strip())
        data.sort()
        print "this user has {0} questions in his account: \n {1}".format(len(data), data)
        return data

def get_employer_dashboard(instance):
    data = list()

    if is_uncomplete(instance):
        return data
    else:
        if is_front(instance):
            jobs_container = instance.find_element_by_xpath('//div[@class="col-xs-9"]')
            jobs_counter = len(jobs_container.find_elements_by_xpath('//div[@ng-repeat="job in jobs track by job.id"]'))

            for item in xrange(1, jobs_counter+1):
                title = jobs_container.find_element_by_xpath(
                '//div[@ng-repeat="job in jobs track by job.id"][%d]/descendant::span[@class="title t-link f-size-17 ng-binding"]'%item)\
                    .get_attribute("textContent")
                candidates_number = jobs_container.find_element_by_xpath(
                '//div[@ng-repeat="job in jobs track by job.id"][%d]/descendant::span[@class="count ng-binding"]'%item)\
                    .get_attribute("textContent")

                data.append((title.strip(), candidates_number))
        else:
            jobs_container = instance.find_element_by_xpath('//div[@class="panel-pane pane-views pane-campaigns"]')
            jobs_counter = len(jobs_container.find_elements_by_xpath('//div[@class="list-campaign-title"]'))

            for item in xrange(1, jobs_counter+1):

                title = jobs_container.find_element_by_xpath(
                    '//div[@class="view-content"]/div[%d]/div[2]/descendant::span[@class="list-jobtitle"]/a'%item)\
                    .get_attribute("textContent")
                candidates_number = jobs_container.find_element_by_xpath('//div[@class="view-content"]/div[%d]/div[3]/span'%item)\
                    .get_attribute("textContent")
                data.append((title.strip(), candidates_number))
    data.sort()
    print "this user has %d campaigns in his dashboard"%len(data)
    print data
    return data

def get_jobseeker_dashboard(instance):
    driver = instance
    data = list()

    if is_uncomplete(instance):
        return data
    else:
        wait(2)
        if is_front(instance):
            job_container = driver.find_element_by_xpath('//jbt-jobseeker-dashboard-jobs/descendant::div[@class="tab-content fw"]')
            jobs_counter = len(job_container.find_elements_by_xpath(
                '//div[@class="fw ng-scope"]/div[@ng-repeat="jobRow in tab.jobs  track by $index"]'))
            for item in xrange(1, jobs_counter+1):
                title = job_container.find_element_by_xpath(
                    '//div[@ng-repeat="jobRow in tab.jobs  track by $index"][%d]/descendant::a[@class="set-c-title ng-binding"]'%item)\
                    .get_attribute("textContent")
                data.append(title.strip())
        else:
            job_container = driver.find_element_by_xpath('//div[@class="right-middle-b "]')
            jobs_counter = len(job_container.find_elements_by_xpath('//li[@class="app-func"]/span/b/a'))
            for item in xrange(1, jobs_counter+1):
                title = job_container.find_element_by_xpath('//li[@class="app-func"][%d]/span/b/a'%item)\
                    .get_attribute('textContent')
                data.append(title.strip())

        print "this jobseeker has {0} job campaigns on his dashboard".format(len(data))
        data.sort()
        print data
        return data

def search_job(instance, job_name, location, answer=None):
    driver = instance
    driver.find_element_by_xpath("//a[@href='/search']").click()
    # driver.find_element_by_xpath('//*[text()="Full-time"]').click()
    place = driver.find_element_by_xpath('//input[@ng-model="search.location"]')
    place.clear()
    place.send_keys(location)
    wait(1)
    position = driver.find_element_by_xpath("//input[@ng-model='search.title']")
    position.clear()
    position.send_keys(job_name)
    wait(3)
    driver.find_element_by_partial_link_text(job_name).click()

    wait_until(instance, '//div[@class="sticky-apply ng-scope"]')
    if is_element_visible(driver,'//button[contains(text(),"Apply for this Job")]', 1):
        application = driver.find_element_by_xpath('//button[contains(text(),"Apply for this Job")]')
        application.click()
        if is_element_visible(driver, '//div[@class="ngdialog-content"]', 2):
            if answer.lower() == "yes":
                driver.find_element_by_xpath(
                    '//div[@class="ngdialog-content"]/descendant::label[@ng-class="{active: answer == 1}"]').click()
                driver.find_element_by_xpath(
                    '//div[@class="ngdialog-content"]/descendant::button[contains(text(),"Apply")]').click()
            else:
                driver.find_element_by_xpath(
                    '//div[@class="ngdialog-content"]/descendant::label[@ng-class="{active: answer == 0}"]').click()
                driver.find_element_by_xpath(
                    '//div[@class="ngdialog-content"]/descendant::button[contains(text(),"Apply")]').click()

        print "have applied to the job campaign"
    else:
        print "jobseeker has already applied to this job campaign"

def pass_assesment(instance, jobs_number, default_list):
    pass
    # driver = instance
    #
    # for item in xrange(1, jobs_number+1):

def get_language(instance):
    driver = instance
    data = []

    if is_uncomplete(instance):
        return data
    else:
        if is_front(instance):
            driver.find_element_by_xpath('//a[@ui-sref="zumay_page"]').click()
            language_container = driver.find_element_by_xpath(
                '//div[@class="zumay_page-content-block languages-block editable-section"]/descendant::div[@class="zumay_page-languages-list"]')
            language_counter = len(language_container.find_elements_by_xpath('div'))

            for item in xrange(1, language_counter+1):
                language = language_container.find_element_by_xpath('//div[%d]/h2[@class="subtitle dark ng-binding"]'%item).\
                    get_attribute("textContent")
                data.append(language.strip())

        else:
            driver.find_element_by_link_text("My Zumay").click()
            language_container = driver.find_element_by_xpath('//div[@id="languages"]')
            language_counter = len(language_container.find_elements_by_xpath(
                '//div[@class="field-collection-container clearfix"]/descendant::div[@class="field field-name-field-languages-single-dropdown field-type-taxonomy-term-reference field-label-hidden"]'))

            for item in xrange(1, language_counter+1):
                language = language_container.find_element_by_xpath(
                    '//div[%d]/div/div[@class="field field-name-field-languages-single-dropdown field-type-taxonomy-term-reference field-label-hidden"]'%item).\
                    get_attribute("textContent")
                data.append(language.strip())

    print "this user has %d languages"%language_counter
    data.sort()
    print data
    return data

def get_education(instance):
    driver = instance
    data = []

    if is_uncomplete(instance):
        return data
    else:
        if is_front(instance):
            driver.find_element_by_xpath('//a[@ui-sref="zumay_page"]').click()
            education_container = driver.find_element_by_xpath(
                '//div[@class="zumay_page-content-block education-block editable-section"]/div[3]/div[@class="block-body"]')
            education_counter = len(education_container.find_elements_by_xpath('div'))

            for item in xrange(1, education_counter+1):
                education = education_container.find_element_by_xpath(
                    'div[%d]/descendant::a[@ng-bind="education_xp.university.name"]'%item).\
                    get_attribute("textContent")
                data.append(education.strip())

        else:
            driver.find_element_by_link_text("My Zumay").click()
            education_container = driver.find_element_by_xpath(
                '//div[@id="education"]/div/div[@class="pane-content"]/descendant::div[@class="field-collection-container clearfix"]')
            education_counter = len(education_container.find_elements_by_xpath('section'))

            for item in xrange(1, education_counter+1):
                education = education_container.find_element_by_xpath(
                    'section[%d]/descendant::div[@class="field field-name-field-text-single-organization field-type-text field-label-hidden"]'%item).\
                    get_attribute("textContent")
                data.append(education.strip())

    print "this user has %d education records"%education_counter
    data.sort()
    print data
    return data

def get_experience(instance):
    driver = instance
    data = []

    if is_uncomplete(instance):
        return data
    else:
        if is_front(instance):
            if is_front(instance):
                driver.find_element_by_xpath('//a[@ui-sref="zumay_page"]').click()
                experince_container = driver.find_element_by_xpath(
                    '//div[@class="zumay_page-content-block work-exp-block editable-section"]/div[3]/div[@class="block-body no-pad"]')
                experince_counter = len(experince_container.find_elements_by_xpath('div'))

                for item in xrange(1, experince_counter+1):
                    experince = experince_container.find_element_by_xpath(
                        'div[%d]/descendant::h3/div/span[@ng-bind="xp_place.position"]'%item).\
                        get_attribute("textContent")
                    data.append(experince.strip())


        else:
            driver.find_element_by_link_text("My Zumay").click()
            experince_container = driver.find_element_by_xpath(
                '//div[@id="experience"]/div/div[@class="pane-content"]/descendant::div[@class="field-collection-container clearfix"]')
            experince_counter = len(experince_container.find_elements_by_xpath('section'))

            for item in xrange(1, experince_counter+1):
                experince = experince_container.find_element_by_xpath('section[%d]/div/div[1]'%item).\
                    get_attribute("textContent")
                data.append(experince.strip())

    print "this user has %d experience records"%experince_counter
    data.sort()
    print data
    return data

def get_skills(instance):
    driver = instance
    data = []

    if is_uncomplete(instance):
        return data
    else:
        if is_front(instance):
            if is_front(instance):
                driver.find_element_by_xpath('//a[@ui-sref="zumay_page"]').click()
                experince_container = driver.find_element_by_xpath(
                    '//div[@class="zumay_page-content-block work-exp-block editable-section"]/div[3]/div[@class="block-body no-pad"]')
                experince_counter = len(experince_container.find_elements_by_xpath('div'))

                for item in xrange(1, experince_counter+1):
                    experince = experince_container.find_element_by_xpath(
                        'div[%d]/descendant::h3/div/span[@ng-bind="xp_place.position"]'%item).\
                        get_attribute("textContent")
                    data.append(experince.strip())


        else:
            driver.find_element_by_link_text("My Zumay").click()
            experince_container = driver.find_element_by_xpath(
                '//div[@id="experience"]/div/div[@class="pane-content"]/descendant::div[@class="field-collection-container clearfix"]')
            experince_counter = len(experince_container.find_elements_by_xpath('section'))

            for item in xrange(1, experince_counter+1):
                experince = experince_container.find_element_by_xpath('section[%d]/div/div[1]'%item).\
                    get_attribute("textContent")
                data.append(experince.strip())

    print "this user has %d experience records"%experince_counter
    data.sort()
    print data
    return data


if __name__ == '__main__':
    driver = set_instance("http://front.jobularity.com")
    login(driver, "jobseeker", "testinginbox2@gmail.com", "test")
    x = get_language(driver)
    print x
    y = get_education(driver)
    print y
    z = get_experience(driver)
    print z