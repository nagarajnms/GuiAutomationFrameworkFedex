from base.helper import element_is_visible_by_xpath
from base.basepage import BasePage


class Tracking(BasePage):
    """Page Object for the Tracking page
    Contains locator details and methods pertaining to the tracking page
    """
    def __init__(self, driver, fluent_wait=20):
        super().__init__(driver, fluent_wait)

    @property
    def tracking_results_single_item_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//div[@class="notification__message text-left"]'))

    @property
    def tracking_results_multiple_items_summary_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//h1[text()="Summary Tracking results"]'))

    @property
    def tracking_results_multiple_items_text_element(self):
        return self.wait.until(element_is_visible_by_xpath('//span[@class="systemErrorMessageTop"]'))

    def validate_track_result_single_item(self):
        """Validates the tracking details via single item tracking option
        PS: validating a dummy tracking id"""
        element = self.tracking_results_single_item_text_element
        return "retrieve your tracking results" in element.text

    def validate_track_result_multi_items(self):
        """Validates the info message displayed about the tracking items
        PS: Since the dummy tracking IDs are being used here, the items can't be actually tracked and the negative scenario is validated
        """
        self.tracking_results_multiple_items_summary_text_element
        element = self.tracking_results_multiple_items_text_element
        return "we are unable to retrieve your tracking results" in element.text
