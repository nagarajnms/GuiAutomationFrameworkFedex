from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from functools import wraps


def element_is_visible_by_id(element_id):
    return EC.visibility_of_element_located((By.ID, element_id))


def element_is_visible_by_xpath(element_xpath):
    return EC.visibility_of_element_located((By.XPATH, element_xpath))


def element_is_clickable_by_xpath(element_xpath):
    return EC.element_to_be_clickable((By.XPATH, element_xpath))


# def save_screenshot(driver):
#     total_width = driver.execute_script("return document.body.parentNode.scrollWidth")
#     total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
#
#     # Setting screen size twice because one is not enough for Selenium :)
#     driver.set_window_size(total_width, total_height)
#     driver.set_window_size(total_width, total_height)
#
#     now = datetime.now()
#     path = (
#         "_".join([driver.screenshot_path, now.strftime("%Y%m%d_%H%M%S%f")])
#         + "_exception.png"
#     )
#     driver.get_screenshot_as_file(path)


def screenshot_on_error(test):
    """Taking screenshot on error

    This decorators will take a screenshot of the browser
    when the test failed or when exception raised on the test.
    Screenshot will be saved as PNG inside screenshots folder.

    """

    @wraps(test)
    def wrapper(*args, **kwargs):
        try:
            test(*args, **kwargs)
        except:
            # test_object = args[0]
            # testcase_value = str(test_object)
            # '''
            # Fetching the name of the test case
            # '''
            # testcase_id = testcase_value.split(" ", 1)
            # testcase_name = testcase_id[0]
            # log.info("Test case name :" + testcase_name)
            # '''
            # Fetching the class name for the test case
            # '''
            # testcase_class_id = testcase_value.split(".", 1)
            # testcase_class = testcase_class_id[1].split(")", 1)
            # testcase_class_name = testcase_class[0]
            # log.info("Test case class name :" + testcase_class_name)
            # screenshot_dir = test_object.tnglogs_location + '/screenshots'
            # if not os.path.exists(screenshot_dir):
            #     os.makedirs(screenshot_dir)
            # date_string = datetime.datetime.now().strftime(
            #     '%m%d%y-%H%M%S')
            # filename = '%s/%s-%s-%s.png' % (screenshot_dir, testcase_class_name, testcase_name, date_string)
            # log.info("Capturing the screenshot for the error noticed")
            # test_object.partner_portal_control.driver().save_screenshot(filename)
            print("Printing Args ^^^^^^^^^^^^^")
            for arg in args:
                print(f"Argument is: {arg}")
            # driver = args[0]
            # driver.get_screenshot_as_file("sample.png")
            raise

    return wrapper