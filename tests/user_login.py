__author__ = 'Steve'

import unittest
from auto.Instance import set_instance, get_object_form_csv
from auto.BasePage import enter_page

class Test(unittest.TestCase):

    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True

    def test1_login_methods(self):
        # load browser instance
        instance = set_instance()

        # test login email method
        jobseeker1 = get_object_form_csv(user_name="Robert")
        test = enter_page(instance)
        test.login(jobseeker1)
        test.logout()

        # test facebook login method
        jobseeker2 = get_object_form_csv(user_name="David")
        test.login(jobseeker2)
        test.logout()

        # test tweeter login method
        jobseeker3 = get_object_form_csv(user_name="Louisa")
        test.login(jobseeker3)
        test.logout()

        # test linkedin login method
        jobseeker4 = get_object_form_csv(user_name="Jeefrey")
        test.login(jobseeker4)
        test.logout()
        # close the browser instance
        test.close()

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)

if __name__ == '__main__':
    unittest.main()
