__author__ = 'Steve'

from auto.ZumayPage import search_page
from auto.Instance import set_instance, get_object_form_csv, dict_iterator, get_object
from auto.BasePage import enter_page

def user_applies_jobs(user):
    applicant = get_object_form_csv(user_name=user)
    instance = set_instance()
    browser = enter_page(instance)
    browser.login(applicant)
    browser = search_page(instance)

    for raw_job in dict_iterator("demo_jobcampains.csv"):
        job = get_object(raw_job)
        browser.search_job(job)
        browser.apply_to_job(job)

def users_apply_job(campaign_name):
    instance = set_instance()
    job_campaign = get_object_form_csv(file_name="demo_jobcampains.csv", user_name=campaign_name)

    for raw_applicant in dict_iterator():
        applicant = get_object(raw_applicant)
        browser = enter_page(instance)
        browser.login(applicant)
        browser = search_page(instance)
        browser.search_job(job_campaign)
        browser.apply_to_job(job_campaign)
        browser.logout()

if __name__ == '__main__':
    # user_applies_jobs("Dian")
    users_apply_job("Sales and Marketing Coordinator")