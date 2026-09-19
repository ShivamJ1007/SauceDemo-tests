from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WaitHelper:
    def __init__(self, driver, timeout=40):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        
    def wait_for_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))  

    def wait_for_all_element_located(self,locator):
        return self.wait.until(EC.visibility_of_all_elements_located(locator))