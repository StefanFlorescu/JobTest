__author__ = 'Steve'

import unittest
from auto.Instance import set_instance, set_user, dict_iterator, user_object
from auto.BasePage import enter_page

def load_user_instance(loop_counter):

    for raw in dict_iterator():
        user = user_object(raw)
        x  = set_instance()
        browser = enter_page(x)
        browser.login(user)
        loop_counter = loop_counter -1
        if loop_counter <= 0:
            break



if __name__ == '__main__':

    # instance = set_instance()
    # jobseeker1 = set_user(user_name="Robert")
    # test = enter_page(instance)
    # test.login(jobseeker1)
    # test.wait()
    # test.logout()
    # jobseeker2 = set_user(user_name="David")
    # test.login(jobseeker2)
    # test.wait()
    # test.logout()
    # jobseeker3 = set_user(user_name="Louisa")
    # test.login(jobseeker3)
    # test.wait()
    # test.logout()
    # jobseeker4 = set_user(user_name="Jeefrey")
    # test.login(jobseeker4)
    # test.wait()
    # test.logout()
    load_user_instance(20)