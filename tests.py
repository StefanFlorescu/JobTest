__author__ = 'LENOVO4'

from importer import *

dict = getdict("zap.csv")
# dev_instance = set_instance("http://dev.jobularity.com")
# test_instance = set_instance("http://front2.jobularity.com")
default_jobs=("Equipment Maintenance Technician", "Data Analyst")


def test_enter():
    test_instance = set_instance("http://front.jobularity.com")
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        # login(dev_instance, role, key, password)
        # logout(dev_instance)

        login(test_instance, role, key, password)
        i = raw_input("tes: ")
        logout(test_instance)

def test_accounts():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]
        test_instance = set_instance("http://front2.jobularity.com")
        login(test_instance, role, key, password)

def test_user_info():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role == "employer" or role == "team_member":

            login(dev_instance, role, key, "test1")
            y = get_employer_info(dev_instance)
            logout(dev_instance)
            login(test_instance, role, key, password)
            x = get_employer_info(test_instance)
            logout(test_instance)
            print x == y
        if role == "jobseeker":
            login(dev_instance, role, key, "test1")
            y = get_jobseeker_info(dev_instance)
            logout(dev_instance)
            login(test_instance, role, key, password)
            x = get_jobseeker_info(test_instance)
            logout(test_instance)

            print x == y

def test_dashboard_employer():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role == "employer" or role == "team_member":
            login(dev_instance,role, key, "test1")
            x = get_employer_dashboard(dev_instance)
            logout(dev_instance)

            login(test_instance, role, key, password)
            y = get_employer_dashboard(test_instance)
            logout(test_instance)
        else:
            x = None
            y = None

        if x == y:
                print "All ok here"
        else:
            print "something went wrong here, users must be checked for bugs"
        print

def test_dashboard_jobseeker():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]
        wait(3)
        if role== "employer" or role=="team_member":
            return None

        if role == "jobseeker":
            login(dev_instance,role, key, "test1")
            x = get_jobseeker_dashboard(dev_instance)
            logout(dev_instance)

            login(test_instance, role, key, password)
            y = get_jobseeker_dashboard(test_instance)
            logout(test_instance)

        if x==y:
                print "All ok here"
        else:
            print "something went wrong here, users must be checked for bugs"
        print

def test_library_addresses():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role =="employer" or role == "team_member":
            login(dev_instance, role, key, "test1")
            x = get_addresses(dev_instance)
            logout(dev_instance)

            login(test_instance, role, key, password)
            y = get_addresses(test_instance)
            logout(test_instance)

            if x==y:
                print "All ok here"
            else:
                print "something went wrong here, users must be checked for bugs"
            print
        if role == "jobseeker":
            pass

def test_library_videos():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role =="employer":
            login(dev_instance, role, key, "test1")
            x = get_videos(dev_instance)
            logout(dev_instance)

            login(test_instance, role, key, password)
            y = get_videos(test_instance)
            logout(test_instance)

            if x==y:
                print "All ok here"
            else:
                print "something went wrong here, users must be checked for bugs"
            print
        if role == "jobseeker":
            pass

def test_library_questions():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role =="employer" or role == "team_member":
            login(dev_instance, role, key, "test1")
            x = get_questions(dev_instance)
            logout(dev_instance)

            login(test_instance, role, key, password)
            y = get_questions(test_instance)
            logout(test_instance)

            if x==y:
                print "All ok here"
            else:
                print "something went wrong here, users must be checked for bugs"
            print
        if role == "jobseeker":
            pass

def test_apply_jobcampaign(job_name, location, answer):
    test_instance = set_instance("http://front.jobularity.com")
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role == "jobseeker":
            login(test_instance, role, key, password)
            search_job(test_instance, job_name, location, answer)
            logout(test_instance)

def test_pass_assesment():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role == "jobseeker":
            login(test_instance, role, key, password)
            campaign_number = pass_assesment(test_instance)
            print
            logout(test_instance)

def test_pass_codylity():
    pass

def test_pass_smarterer():
    pass

def test_zumay_page():
    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role== "employer" or role=="team_member":
            return None

        if role == "jobseeker":
            login(dev_instance,role, key, "test1")
            x = [get_language(dev_instance), get_education(dev_instance), get_experience(dev_instance)]
            logout(dev_instance)
            print "------------"
            login(test_instance, role, key, password)
            y = [get_language(test_instance), get_education(test_instance), get_experience(test_instance)]
            logout(test_instance)

        if x==y:
                print "All ok here"
                print
        else:
            print "something went wrong here, users must be checked for bugs"
            print

def load_users(counter):

    for key in dict:
        password = dict[key][0]
        role = dict[key][1]

        if role == "jobseeker":
            test_instance = set_instance("http://front.jobularity.com")
            login(test_instance, role, key, password)
            counter = counter - 1
            if counter <= 0:
                break
            else:
                pass

if __name__ == '__main__':
    pass
    # test_accounts()
    test_apply_jobcampaign("Corporate Lawyer", "Moscow", "Yes")
    # test_enter()
    # test_user_info()
    # test_dashboard_employer()
    # test_library_addresses()
    # test_library_questions()
    # test_library_videos()
    # test_zumay_page()
    # test_dashboard_jobseeker()
    # load_users(7)