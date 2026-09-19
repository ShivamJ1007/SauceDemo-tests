from pages.inventorypage import InventoryPage
from pages.loginpage import Login
from utils.user_data_loader import get_user
from utils.wait_helper import WaitHelper

def test_sort_by_price_low_to_high(driver,base_url):
    inventory_page = InventoryPage(driver)
    login = Login(driver)
    wait = WaitHelper(driver)
    user = get_user()

    driver.get(base_url)

    login.login(user["username"],user["password"])
    wait.wait_for_element_visible(inventory_page.INVENTORY_HEADING)

    inventory_page.apply_sort("Price (low to high)")
    actual_price = inventory_page.get_product_prices()
    expected_price = sorted(actual_price)

    assert expected_price == actual_price, f"Products are not sorted from low to high. Actual prices: {actual_price}"
