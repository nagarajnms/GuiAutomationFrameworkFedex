from base.helper import element_is_visible_by_xpath, element_is_visible_by_id
from base.basepage import BasePage


class Login(BasePage):
    """Page Object for the Login page
    Contains locator details and methods pertaining to the Login page
    """

    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def validate_navigation_to_login_page_element(self):
        return self.wait.until(element_is_visible_by_xpath('//span[text()=" CREATE A USER ID FOR AN EXISTING ACCOUNT "]'))

    @property
    def userid_textbox_element(self):
        return self.wait.until(element_is_visible_by_id("userId"))

    @property
    def password_textbox_element(self):
        return self.wait.until(element_is_visible_by_id("password"))

    @property
    def log_in_button_element(self):
        return self.wait.until(element_is_visible_by_id("login-btn"))

    @property
    def username_in_home_page_element(self):
        return self.wait.until(element_is_visible_by_xpath(f'//span[@class ="fxg-user-options__sign-in-text"]'))

    def login(self, userId, password):
        """login with user credentials"""
        self.validate_navigation_to_login_page_element
        print(f"The user_email and password are: {userId} and {password}")
        element = self.userid_textbox_element
        element.clear()
        element.send_keys(userId)
        element = self.password_textbox_element
        element.clear()
        element.send_keys(password)
        element = self.log_in_button_element
        element.click()

    def validate_login_successful(self, username):
        """validates the login"""
        try:
            element = self.username_in_home_page_element
            return username in element.text
        except:
            print("Login unsuccessful, please refer to the screenshot")
            return False
