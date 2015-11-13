__author__ = 'Steve'

from auto.AbstractPage import AbstractPage


class BasePage(AbstractPage):

    def facebook_login(self, user):
        self.switch_window()
        driver = self.driver
        driver.find_element_by_id("email").send_keys(user.email)
        driver.find_element_by_id("pass").send_keys(user.password)
        driver.find_element_by_name("login").click()
        self.switch_window_back()

    def twitter_login(self, user):
        self.switch_window()
        driver = self.driver
        driver.find_element_by_xpath('//label[@for="username_or_email"]').send_keys(user.email)
        driver.find_element_by_xpath('//label[@for="password"]').send_keys(user.password)
        driver.find_element_by_xpath('//input[@value="Sign In"]').click()
        self.switch_window_back()

    def linkedin_login(self, user):
        self.switch_window()
        driver = self.driver
        driver.find_element_by_xpath('//li[@class="email-input"]/descendant::input').send_keys(user.email)
        driver.find_element_by_xpath('//li[@class="password-input"]/descendant::input').send_keys(user.password)
        driver.find_element_by_xpath('//input[@value="Allow access"]').click()
        self.switch_window_back()


    def login(self, user):
        self.driver.find_element_by_css_selector("button.identif_butt").click()
        driver = self.driver.find_element_by_xpath('//div[@class="ngdialog-content"]/div[@class="login-form"]')
        if user.login_method == "email":
            driver.find_element_by_name("usermail").send_keys(user.email)
            driver.find_element_by_xpath("//input[@name='password']").send_keys(user.password)
            driver.find_element_by_css_selector("button.sign-in").click()
        elif user.login_method == "facebook":
            driver.find_element_by_xpath('//ul[@class="social-list"]/descendant::i[@class="fa fa-facebook"]').click()
            self.facebook_login(user)
        elif user.login_method == "twitter":
            driver.find_element_by_xpath('//ul[@class="social-list"]/descendant::i[@class="fa fa-twitter"]').click()
            self.twitter_login(user)
        elif user.login_method == "linkedin":
            driver.find_element_by_xpath('//ul[@class="social-list"]/descendant::i[@class="fa fa-linkedin"]').click()
            self.linkedin_login(user)


    def logout(self):
        driver = self.driver
        driver.find_element_by_class_name("user-img-x").click()
        driver.find_element_by_link_text("Log out").click()

    def register(self, user):
        self.driver.find_element_by_xpath('//a[@ui-sref="user.register"]').click()
        driver = self.driver.find_element_by_id('register_form')

        if user.login_method == "email":
            driver.find_element_by_name("firstName").send_keys(user.name)
            driver.find_element_by_name("lastName").send_keys(user.surename)
            driver.find_element_by_name("email").send_keys(user.email)
            driver.find_element_by_name("password").send_keys(user.password)
            driver.find_element_by_name("confirmPassword").send_keys(user.password)
            driver.find_element_by_xpath('//label[@ng-class="{active: user.accountType == \'%s\'}"]'%user.role).click()
            if user.role == "jobseeker":

                driver.find_element_by_xpath('//div[@placeholder="Enter an industry..."]').click()
                self.select_by_text("xpath", '//ul/li[@class="ui-select-choices-group"]', user.industry)
            driver.find_element_by_xpath('//button[contains(text(),"Create a new account")]').click()

        elif user.login_method == "facebook":
            driver.find_element_by_xpath('//i[@class="fa fa-facebook"]').click()
            self.facebook_login(user)
            self.wait_until('//h1[contains(text()," Let\'s Get")]')
            driver = self.driver.find_element_by_id('register_form')
            driver.find_element_by_name("email").send_keys(user.email)
            driver.find_element_by_xpath('//select[@name="accountType"]/option[@value="%s"]'%user.role).click()
            driver.find_element_by_xpath('//button[contains(text(),"Continue")]')

        elif user.login_method == "twitter":
            driver.find_element_by_xpath('//i[@class="fa fa-twitter"]').click()
            self.twitter_login(user)
            self.wait_until('//h1[contains(text()," Let\'s Get")]')
            driver = self.driver.find_element_by_id('register_form')
            driver.find_element_by_name("email").send_keys(user.email)
            driver.find_element_by_xpath('//select[@name="accountType"]/option[@value="%s"]'%user.role).click()
            driver.find_element_by_xpath('//button[contains(text(),"Continue")]')

        elif user.login_method == "linkedin":
            driver.find_element_by_xpath('//i[@class="fa fa-linkedin"]').click()
            self.linkedin_login(user)
            self.wait_until('//h1[contains(text()," Let\'s Get")]')
            driver = self.driver.find_element_by_id('register_form')
            # driver.find_element_by_name("email").send_keys(user.email)
            driver.find_element_by_xpath('//select[@name="accountType"]/option[@value="%s"]'%user.role).click()
            driver.find_element_by_xpath('//button[contains(text(),"Continue")]')


