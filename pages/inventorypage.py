from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from utils.wait_helper import WaitHelper

class InventoryPage:
    # Locators on the Inventory Page
    INVENTORY_HEADING = (By.XPATH, '//span[contains(text(),"Products")]')
    SORTING_LIST = (By.XPATH, "//select[@class='product_sort_container']")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='inventory_item_name ']")
    CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
    ADD_TO_CART_BTNS = (By.XPATH, "//button[@class='btn btn_primary btn_small btn_inventory ']")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    

    def __init__(self, driver:WebDriver):
        self.driver=driver
        self.wait=WaitHelper(driver)
 
    def apply_sort(self,sort_type):
        self.wait.wait_for_element_clickable(self.SORTING_LIST)
        sorting_dropdown = self.driver.find_element(*self.SORTING_LIST)
        select = Select(sorting_dropdown)
        select.select_by_visible_text(sort_type)

    def get_product_prices(self):
        self.wait.wait_for_all_element_located(self.PRICES)
        price_elements = self.driver.find_elements(*self.PRICES)

        prices = []

        for element in price_elements:
            price_text = element.text
            price_without_dollar = price_text.replace("$", "")
            price_number = float(price_without_dollar)
            prices.append(price_number)     
        return prices

    def add_cheapest_and_most_expensive(self):
        products = self.driver.find_elements(*self.PRODUCT_NAMES)
        cheapest_name = products[0].text
        most_expensive_name = products[-1].text
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)

        # First product is the cheapest
        add_buttons[0].click()

        # Find the buttons again because the first button changes to remove product
        add_buttons = self.driver.find_elements(*self.ADD_TO_CART_BTNS)

        # Last product is the most expensive
        add_buttons[-1].click()

        return [cheapest_name, most_expensive_name]

    def get_cart_count(self):
        cart_count = self.driver.find_element(*self.CART_BADGE).text
        return cart_count