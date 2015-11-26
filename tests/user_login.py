__author__ = 'Steve'

<<<<<<< HEAD
# import unittest
from auto.Instance import set_instance, get_object_form_csv, dict_iterator, get_object
=======
import unittest
from auto.Instance import set_instance, get_object_form_csv
>>>>>>> oop
from auto.BasePage import enter_page

class Test(unittest.TestCase):

<<<<<<< HEAD
    for raw in dict_iterator():
        user = get_object(raw)
        instance = set_instance()
        browser = enter_page(instance)
        browser.login(user)
        loop_counter = loop_counter -1
        if loop_counter <= 0:
            break
=======
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
>>>>>>> oop

    def test1_login_methods(self):
        # load browser instance
        instance = set_instance()

        # test login email method
        jobseeker1 = get_object_form_csv(user_name="Robert")
        test = enter_page(instance)
        test.login(jobseeker1)
        test.logout()

<<<<<<< HEAD
if __name__ == '__main__':
# this tests checks that all the login methods are functional
    instance = set_instance()
    jobseeker1 = get_object_form_csv(user_name="Robert")
    test = enter_page(instance)
    test.login(jobseeker1)
    test.wait()
    test.logout()
    jobseeker2 = get_object_form_csv(user_name="David")
    test.login(jobseeker2)
    test.wait()
    test.logout()
    jobseeker3 = get_object_form_csv(user_name="Louisa")
    test.login(jobseeker3)
    test.wait()
    test.logout()
    jobseeker4 = get_object_form_csv(user_name="Jeefrey")
    test.login(jobseeker4)
    test.wait()
    test.logout()
    test.close()
    # load_user_instance(20)
=======
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
>>>>>>> oop
