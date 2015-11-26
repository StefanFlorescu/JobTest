__author__ = 'Steve'

import unittest
from auto.Instance import set_instance, get_user, dict_iterator
from auto.BasePage import enter_page

class Test(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True

    def test1_pages(self):

        # load hiring man browser instance
        employer_instance = set_instance("ie")
        employer_object = get_user("Kevin")
        employer = enter_page(employer_instance)
        employer.login(employer_object)

        # load the recruiter browser instance
        recruiter_instance = set_instance("opera")
        recruiter_object = get_user('Kevyn')
        recruiter = enter_page(recruiter_instance)
        recruiter.login(recruiter_object)

        # load the jobseeker browser instance
        jobseeker_instance = set_instance('firefox')
        jobseeker_object = get_user("Dian")
        jobseeker = enter_page(jobseeker_instance)
        jobseeker.login(jobseeker_object)

        # load the anonymous browser instance
        anonymous_instance = set_instance()
        anonymous = enter_page(anonymous_instance)


        links = ['http://front.jobularity.com/zumay/testinginbox1','http://front.jobularity.com/company/testingsitesqa1447759064/truck-driver-heavy-tractor-trailer']

        for link in links:

            employer.get_url(link)
            employer.wait()
            recruiter.get_url(link)
            recruiter.wait()
            jobseeker.get_url(link)
            jobseeker.wait()
            anonymous.get_url(link)
            anonymous.wait()
            r = raw_input("continue")

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
