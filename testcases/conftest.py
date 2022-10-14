from selenium import webdriver
import pytest
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from base.helper import element_is_clickable_by_xpath
from pages.home import Home


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook implementation to make the result information available in teardown
    Documentation Referred: https://docs.pytest.org/en/latest/example/simple.html#making-test-result-information-available-in-fixtures
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="function")
def browser_setup(request):
    """
    The browser setup fixture will open the GUI via the selenium webdriver and return home page object to the test case.
    As part of the teardown, if the TC has failed it takes a screenshot before quitting the browser sessions.
    """
    driver = webdriver.Chrome()
    driver.get("https://www.fedex.com/en-gb/home.html")
    driver.maximize_window()
    wait = WebDriverWait(driver, 20)
    element = wait.until(element_is_clickable_by_xpath('//span[text()="English"]'))
    print(element)
    element.click()
    try:
        sleep(2)
        # The Accept Cookies popup is intermittently seen. This is to handle the same.
        driver.find_element(By.XPATH, '//button[text()="ACCEPT ALL COOKIES"]').click()
    except Exception:
        print("The accept Cookies Pop-up is not seen")
    home_page = Home(driver)
    yield home_page
    sleep(3)
    if request.node.rep_call.failed:
        driver.save_screenshot(f".\\screenshots\\{request.node.name}.png")
    driver.quit()


