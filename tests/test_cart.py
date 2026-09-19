from pages.inventorypage import InventoryPage
from pages.loginpage import Login
from utils.user_data_loader import get_user
from utils.wait_helper import WaitHelper
from pages.cart_page import CartPage


def test_add_cheapest_and_most_expensive(driver, base_url):
    inventory_page = InventoryPage(driver)
    login = Login(driver)
    wait = WaitHelper(driver)
    user = get_user()
    
    driver.get(base_url)
    login.login(user["username"],user["password"])
    wait.wait_for_element_visible(inventory_page.INVENTORY_HEADING)
    inventory_page.apply_sort("Price (low to high)")
    inventory_page.add_cheapest_and_most_expensive()

    cart_count = inventory_page.get_cart_count()
    assert cart_count == "2", (f"Expected cart count to be 2, but found {cart_count}")

def test_cart_products(driver,base_url):
    inventory_page = InventoryPage(driver)
    login = Login(driver)
    cart_page = CartPage(driver)
    user = get_user()

    driver.get(base_url)
    login.login(user["username"],user["password"])

    inventory_page.apply_sort("Price (low to high)")

    expected_products = (inventory_page.add_cheapest_and_most_expensive())
    assert inventory_page.get_cart_count() == "2"

    inventory_page.driver.find_element(*inventory_page.CART).click()
    assert cart_page.get_cart_item_count() == 2

    actual_products = cart_page.get_product_names()

    assert sorted(actual_products) == sorted(expected_products), (
        f"Expected {expected_products}, but found {actual_products}"
    )
    cart_page.click_checkout_button()