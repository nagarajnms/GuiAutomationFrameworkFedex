from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    """The Base POM page which will be inherited by all the other POM pages"""

    def __init__(self, driver, fluent_wait=20):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, fluent_wait)
        self.actions = ActionChains(self.driver)
        self.wait.until(self.is_page_loaded)

    def is_page_loaded(self, *args):
        """Waits for a page to be completely loaded"""
        return self.driver.execute_script("return document.readyState == 'complete'")