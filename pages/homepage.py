from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class Homepage:
    def __init__(self, driver:WebDriver):
        self.driver=driver

    INVENTORY_HEADING = (By.XPATH, '//div[contains(text(),"Products")]')
    SORTING_LIST = (By.XPATH, "//select[@class='product_sort_container']")
    CART = (By.XPATH, "//a[@class='shopping_cart_link']")
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
    ADD_TO_CART = (By.ID, "add-to-cart-sauce-labs-backpack")

    def apply_sort(self,sort_type):
        select = Select(self.SORTING_LIST)
        select.select_by_visible_text(sort_type)
    