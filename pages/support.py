from time import sleep
import re

from base.helper import element_is_visible_by_id, element_is_visible_by_xpath
from base.basepage import BasePage


class Support(BasePage):
    """Page Object for the Support page
    Contains locator details and methods pertaining to the Support page
    """
    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def new_customer_centre_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[contains(text(), "New Customer Centre")]'))

    @property
    def fedex_locations_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[contains(text(), "Find FedEx locations")]'))

    @property
    def find_locations_textbox_element(self):
        return self.wait.until(element_is_visible_by_id('DirectorySearchInput'))

    @property
    def search_button_element(self):
        return self.wait.until(element_is_visible_by_xpath('//span[text()="Search"]'))

    @property
    def results_summary_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//div[@class="ResultSummary"]'))

    def validate_new_customer_center_page(self):
        """Validates navigation to the new customer centre sub-page from Support dropdown"""
        element = self.new_customer_centre_text_element
        return bool(element)

    def validate_locations_page(self):
        """Validates navigation to the locations sub-page from Support dropdown"""
        element = self.fedex_locations_text_element
        return bool(element)

    def find_fedex_location(self, location="AMSTELVEEN, NETHERLANDS"):
        """Enters the location details to search the nearest fedex outlets and
        then validates if the nearest locations were displayed"""
        element = self.find_locations_textbox_element
        self.actions.move_to_element(element).pause(2).click().send_keys(location).perform()
        element = self.search_button_element
        element.click()
        sleep(5)
        result_summary = self.results_summary_text_element.text
        print(result_summary)
        return re.match(r"[0-9]+ LOCATIONS NEAR", result_summary)

