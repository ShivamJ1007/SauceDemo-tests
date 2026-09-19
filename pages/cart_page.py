from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper


class CartPage:
    CART_HEADING = (By.XPATH, '//span[contains(text(),"Your Cart")]')
    CART_ITEMS = (By.XPATH, "//div[@class='cart_item']")
    PRODUCT_NAMES = (By.XPATH, "//div[@class='inventory_item_name']")
    PRODUCT_PRICES = (By.XPATH, "//div[@class='inventory_item_price']")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)

    def get_cart_item_count(self):
        cart_items = self.wait.wait_for_all_element_located(self.CART_ITEMS)
        return len(cart_items)
    
    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def get_product_names(self):
        product_elements = self.driver.find_elements(*self.PRODUCT_NAMES)

        product_names = []

        for element in product_elements:
            product_names.append(element.text)

        return product_names

    def get_product_prices(self):
        price_elements = self.driver.find_elements(*self.PRODUCT_PRICES)

        product_prices = []

        for element in price_elements:
            product_prices.append(element.text)

        return product_prices