from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_helper import WaitHelper


class CheckoutPage:

    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    OVERVIEW_PRODUCT_NAMES = (By.CLASS_NAME,"inventory_item_name")
    OVERVIEW_PRODUCT_PRICES = (By.CLASS_NAME,"inventory_item_price")
    ITEM_TOTAL = (By.CLASS_NAME,"summary_subtotal_label")
    TAX = (By.CLASS_NAME,"summary_tax_label")
    FINAL_TOTAL = (By.CLASS_NAME,"summary_total_label")
    FINISH_BUTTON = (By.ID,"finish")

    CONFIRMATION_TEXT = (By.ID, "checkout_complete_container")
    BACK_HOME_BTN = (By.ID, "back-to-products")
    GENERATE_PDF_ORDER = (By.ID, "generate-pdf-order")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver, 10)

    def enter_checkout_information(self,first_name,last_name,postal_code):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.POSTAL_CODE).send_keys(postal_code)

    def get_page_title(self):
        return self.wait.wait_for_element_visible(self.PAGE_TITLE).text

    def get_overview_product_names(self):
        product_elements = self.driver.find_elements(*self.OVERVIEW_PRODUCT_NAMES)

        product_names = []

        for element in product_elements:
            product_names.append(element.text)

        return product_names

    def get_overview_product_prices(self):
        price_elements = self.driver.find_elements(
            *self.OVERVIEW_PRODUCT_PRICES
        )

        product_prices = []

        for element in price_elements:
            product_prices.append(element.text)

        return product_prices

    def get_item_total(self):
        return self.driver.find_element(*self.ITEM_TOTAL).text

    def get_tax(self):
        return self.driver.find_element(*self.TAX).text

    def get_final_total(self):
        return self.driver.find_element(*self.FINAL_TOTAL).text

    def click_finish(self):
        self.driver.find_element(*self.FINISH_BUTTON).click()

    def get_confirmation_text(self):
        return self.driver.find_element(*self.CONFIRMATION_TEXT).text

    def download_order_pdf(self):
        download_button = self.wait.wait_for_element_clickable(
            self.GENERATE_PDF_ORDER
        )

        download_button.click()