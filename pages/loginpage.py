from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper

class Login:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.wait= WaitHelper(driver)

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def login(self, username, password):
        self.wait.wait_for_element_visible(self.USERNAME)
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()