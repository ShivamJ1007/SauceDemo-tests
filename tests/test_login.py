from pages.loginpage import Login
from utils.user_data_loader import get_user
from utils.config_loader import load_config


# Load config and test data
config = load_config()

def test_login(driver):
    driver.get("https://www.saucedemo.com/")
    login_page = Login(driver)
    user = get_user()
    login_page.login(user["username"],user["password"])
    assert driver