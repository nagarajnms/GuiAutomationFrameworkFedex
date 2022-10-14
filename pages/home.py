from time import sleep
from selenium.webdriver.common.by import By

from base.helper import element_is_visible_by_id, element_is_visible_by_xpath
from pages.login import Login
from pages.tracking import Tracking
from pages.shipping import Shipping
from pages.support import Support
from pages.account import Account
from base.basepage import BasePage


class Home(BasePage):
    """Contains locator details and methods pertaining to the home(landing) page of the GUI """

    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def return_to_home_element(self):
        return self.wait.until(element_is_visible_by_xpath('//span[@class="fxg-mouse"]/img[@class="fxg-header__logo"]'))

    @property
    def signup_login_element(self):
        return self.driver.find_element(By.XPATH, '//span[text() = "Sign Up/Log In "]')

    @property
    def login_element(self):
        return self.driver.find_element(By.XPATH, '//a[@title="LOG IN"]')

    @property
    def track_element(self):
        return self.driver.find_element(By.XPATH, '//span[text()="TRACK"]')

    @property
    def tracking_number_element(self):
        return self.wait.until(element_is_visible_by_id("trackingnumber"))

    @property
    def single_track_button_element(self):
        return self.wait.until(element_is_visible_by_id("btnSingleTrack"))

    @property
    def multiple_track_button_element(self):
        return self.wait.until(element_is_visible_by_id("btnMultiTrack"))

    @property
    def multiple_tracking_numbers_element(self):
        return self.driver.find_element(By.XPATH, '//a[@aria-label="Multiple Tracking Numbers"]')

    @property
    def tracking_dropdown_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a/span[contains(text(), "Tracking")]'))

    @property
    def trackingid_textbox_element(self):
        return self.wait.until(element_is_visible_by_id("trackingModuleTrackingNum"))

    @property
    def track_button_in_dropdown_element(self):
        return self.wait.until(element_is_visible_by_xpath('//button[@aria-label="Click here to track your package"]'))

    @property
    def shipping_dropdown_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a/span[contains(text(), "Shipping")]'))

    @property
    def ship_without_account_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "Ship without account")]'))

    @property
    def select_returns_from_shipping_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "Returns")]'))

    @property
    def activate_ask_fedex_element(self):
        return self.wait.until(element_is_visible_by_xpath('//div[@class="va_icon"]'))

    @property
    def type_here_assistant_textbox_element(self):
        return self.wait.until(element_is_visible_by_xpath('//span[text()="TYPE HERE"]'))

    @property
    def support_dropdown_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a/span[contains(text(), "Support")]'))

    @property
    def new_customer_center_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "New Customer Centre")]'))

    @property
    def chat_response_element(self):
        return self.wait.until(element_is_visible_by_xpath('//div[@class="nw_AgentSays nw_AgentLastAnswer"]'))

    @property
    def chat_message_submit_element(self):
        return self.wait.until(element_is_visible_by_xpath('//div[text()="SUBMIT"]'))

    @property
    def locations_button_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "Locations")]'))

    @property
    def account_dropdown_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a/span[contains(text(), "Account")]'))

    @property
    def manage_billing_online_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "Manage Billing Online")]'))

    @property
    def account_management_element(self):
        return self.wait.until(element_is_visible_by_xpath('//a[contains(text(), "Account Management")]'))

    def return_to_home(self):
        """Return to home page from anywhere else in the website."""
        element = self.return_to_home_element
        element.click()

    def login(self):
        """Navigate to the login page
        Returns Login Page object"""
        signup_login_element = self.signup_login_element
        signup_login_element.click()
        login_link = self.login_element
        login_link.click()
        return Login(self.driver)

    def track_item_from_homepage(self, tracking_id="1234"):
        """Enter tracking details for single item
         Returns Tracking Page object."""
        element = self.track_element
        element.click()
        element = self.tracking_number_element
        element.clear()
        element.send_keys(tracking_id)
        sleep(3)
        element = self.single_track_button_element
        sleep(2)
        element.click()
        return Tracking(self.driver)

    def track_multiple_items_from_homepage(self, *args):
        """Enter tracking details for multiple items from home page.
         Returns Tracking Page object."""
        element = self.track_element
        element.click()
        element = self.multiple_tracking_numbers_element
        element.click()
        for count, arg in enumerate(args, start=1):
            tracking_number = f"TRACKING NUMBER 0{count}"
            xpath = f'//span[text() = "{tracking_number}"]'
            elem = self.wait.until(element_is_visible_by_xpath(xpath))
            self.actions.move_to_element(elem).pause(2).click().send_keys(arg)
        element = self.multiple_track_button_element
        sleep(2)
        element.click()
        return Tracking(self.driver)

    def select_tracking_dropdown(self):
        """Selects Tracking dropdown in home page"""
        element = self.tracking_dropdown_element
        element.click()

    def insert_tracking_id_and_track(self, tracking_id="1234"):
        """Inserts tracking number and clicks track from tracking dropdown
        Returns Tracking page object."""
        element = self.trackingid_textbox_element
        element.clear()
        element.send_keys(tracking_id)
        element = self.track_button_in_dropdown_element
        element.click()
        return Tracking(self.driver)

    def select_shipping_dropdown(self):
        """Selects Shipping dropdown in home page"""
        element = self.shipping_dropdown_element
        element.click()

    def select_ship_without_account(self):
        """Selects the Ship without account from Shipping dropdown in home page
        Returns Shipping Page object."""
        element = self.ship_without_account_element
        element.click()
        return Shipping(self.driver)

    def select_returns_from_shipping_dropdown(self):
        """Selects the Returns option from Shipping dropdown in home page
        Returns Shipping Page object."""
        element = self.select_returns_from_shipping_element
        element.click()
        return Shipping(self.driver)

    def activate_ask_fedex(self):
        """Opens up the Ask Fedex Chat window"""
        element = self.activate_ask_fedex_element
        element.click()

    def ask_assistant(self, message):
        """Enters the message in the chat window and grabs the response"""
        element = self.type_here_assistant_textbox_element
        print(f"Question/Message to be sent in the chat box:\n{message}")
        self.actions.move_to_element(element).pause(2).click().send_keys(message).perform()
        element = self.chat_message_submit_element
        element.click()
        sleep(3)
        element = self.chat_response_element
        print(f"\nChat Response received: \n{element.text}")
        return "To get an estimate of the shipping charges" in element.text

    def select_support_dropdown(self):
        """Selects Support dropdown in home page"""
        element = self.support_dropdown_element
        element.click()

    def select_new_customer_center(self):
        """Clicks the New Customer Centre option from the Support dropdown in home page
        Returns Support page object"""
        element = self.new_customer_center_element
        element.click()
        return Support(self.driver)

    def select_locations(self):
        """Clicks the Locations option from the Support dropdown in home page
        Returns Support page object"""
        element = self.locations_button_element
        element.click()
        return Support(self.driver)

    def select_account_dropdown(self):
        """Selects Account dropdown from the home page"""
        element = self.account_dropdown_element
        element.click()

    def navigate_to_manage_billing(self):
        """Selects the Manage Billing option from the Account Dropdown
        Returns Account Page object"""
        element = self.manage_billing_online_element
        element.click()
        return Account(self.driver)

    def navigate_to_account_management(self):
        """Selects the Account Management option from the Account Dropdown
        Returns Account Page object"""
        element = self.account_management_element
        element.click()
        return Account(self.driver)
