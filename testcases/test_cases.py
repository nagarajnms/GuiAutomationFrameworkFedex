from configfiles.test_data import *


def test_login(browser_setup):
    """Verify the login feature"""
    home_page = browser_setup
    assert home_page.is_page_loaded(), "Failed to load the home page"
    login_page = home_page.login()
    login_page.login(user['email'], user['password'])
    success = login_page.validate_login_successful(user['username'])
    assert success, "Login unsuccessful"


def test_track_item_from_home_page(browser_setup):
    """Tracking from home page for a single item"""
    home_page = browser_setup
    tracking_page = home_page.track_item_from_homepage(tracking_ids['single_item'])
    track_result = tracking_page.validate_track_result_single_item()
    assert track_result, "Unable to retrieve the tracking information"


def test_track_multiple_items_from_home_page(browser_setup):
    """Tracking from home page for multiple items"""
    home_page = browser_setup
    tracking_page = home_page.track_multiple_items_from_homepage(tracking_ids['multiple_items'])
    track_result = tracking_page.validate_track_result_multi_items()
    assert track_result, "Unable to retrieve the tracking information"


def test_ship_an_item_without_account(browser_setup):
    """Ship an item without account"""
    home_page = browser_setup
    home_page.select_shipping_dropdown()
    shipping_page = home_page.select_ship_without_account()
    result = shipping_page.validate_ship_without_account()
    assert result, "Did not properly navigate to the Ship without account page"


def test_returns_from_shipping_dropdown(browser_setup):
    """Validate the Returns feature"""
    home_page = browser_setup
    home_page.select_shipping_dropdown()
    shipping_page = home_page.select_returns_from_shipping_dropdown()
    result = shipping_page.validate_navigation_to_returns_page()
    assert result, "Did not properly navigate to the Returns page"


def test_fedex_virtual_assistant(browser_setup):
    """Validate the fedex virtual assistant behaviour"""
    home_page = browser_setup
    home_page.activate_ask_fedex()
    message_received = home_page.ask_assistant(ask_assistant_message)
    assert message_received, "Message not received successfully by the assistant"


def test_track_item_from_dropdown_menu(browser_setup):
    """Tracking an item from the tracking dropdown"""
    home_page = browser_setup
    home_page.select_tracking_dropdown()
    tracking_page = home_page.insert_tracking_id_and_track(tracking_ids['single_item'])
    track_result = tracking_page.validate_track_result_single_item()
    assert track_result, "Unable to retrieve the tracking information"


def test_validate_new_customer_center_page(browser_setup):
    """New customer centre page from Support"""
    home_page = browser_setup
    home_page.select_support_dropdown()
    support_page = home_page.select_new_customer_center()
    page_validated = support_page.validate_new_customer_center_page()
    assert page_validated, "Navigation to the New Customer Center Page failed"


def test_validate_locations(browser_setup):
    """Search the nearest fedex locations from any location"""
    home_page = browser_setup
    home_page.select_support_dropdown()
    support_page = home_page.select_locations()
    locations = support_page.validate_locations_page()
    assert locations, "Navigation to Locations page failed"
    found_locations = support_page.find_fedex_location(location)
    assert found_locations, f"Failed to find locations near {location}"


def test_validate_manage_billing_page(browser_setup):
    """Navigate to validate the Manage billing page from Account"""
    home_page = browser_setup
    home_page.select_account_dropdown()
    account_page = home_page.navigate_to_manage_billing()
    page_validated = account_page.validate_billing_online_page()
    assert page_validated, "Navigation to the Manage Billing Page failed"


def test_validate_account_management_page(browser_setup):
    """Validate the Account Management Page"""
    home_page = browser_setup
    home_page.select_account_dropdown()
    account_page = home_page.navigate_to_account_management()
    page_validated = account_page.validate_account_management_page()
    assert page_validated, "Navigation to the Account Management Page failed"

