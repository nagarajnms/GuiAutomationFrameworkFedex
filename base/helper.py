from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def element_is_visible_by_id(element_id):
    return EC.visibility_of_element_located((By.ID, element_id))


def element_is_visible_by_xpath(element_xpath):
    return EC.visibility_of_element_located((By.XPATH, element_xpath))


def element_is_clickable_by_xpath(element_xpath):
    return EC.element_to_be_clickable((By.XPATH, element_xpath))

