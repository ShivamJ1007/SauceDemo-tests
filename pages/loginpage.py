from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Login:
    def __init__(self,driver:WebDriver):
        self.driver = driver

    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN).click()