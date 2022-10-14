from base.helper import element_is_visible_by_xpath
from base.basepage import BasePage


class Account(BasePage):
    """Page Object for the Account page
    Contains locator details and methods pertaining to the Account page
    """
    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def validate_billing_page_navigation_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[contains(text(), "FedEx Billing Online")]'))

    @property
    def validate_account_page_navigation_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[contains(text(), "Account Management")]'))

    def validate_billing_online_page(self):
        """Validates if the navigation to the Online Billing sub-page is successful"""
        element = self.validate_billing_page_navigation_element
        return bool(element)

    def validate_account_management_page(self):
        """Validates if the navigation to the account management sub-page is successful"""
        element = self.validate_account_page_navigation_element
        return bool(element)
