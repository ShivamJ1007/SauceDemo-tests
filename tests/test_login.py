from pages.loginpage import Login
from pages.inventorypage import InventoryPage
from utils.user_data_loader import get_user
from utils.config_loader import load_config
from utils.wait_helper import WaitHelper
import time

# Load config and test data
config = load_config()

def test_login(driver, base_url):
    login_page = Login(driver)
    inventory_page = InventoryPage(driver)
    wait_helper = WaitHelper(driver)
    user = get_user()

    driver.get(base_url)
    login_page.login(user["username"],user["password"])
    wait_helper.wait_for_element_visible(inventory_page.INVENTORY_HEADING)
    assert inventory_page.driver.find_element(*inventory_page.INVENTORY_HEADING).is_displayed(), f"Some Error Occurred while login with {user['username']}"