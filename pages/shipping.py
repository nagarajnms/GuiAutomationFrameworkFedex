from base.helper import element_is_visible_by_xpath
from base.basepage import BasePage


class Shipping(BasePage):
    """Page Object for the Shipping page
    Contains locator details and methods pertaining to the Shipping page
    """
    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def shipping_details_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h3[contains(text(), "Enter your (From) address and the recipient\'s (To) address.")]'))

    @property
    def international_returns_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[contains(text(), "International Returns")]'))

    def validate_ship_without_account(self):
        """Validates the Ship without account sub-page from Shipping"""
        element = self.shipping_details_element
        return bool(element)

    def validate_navigation_to_returns_page(self):
        """Validates the navigation to the Returns sub-page from Shipping"""
        element = self.international_returns_text_element
        return bool(element)



