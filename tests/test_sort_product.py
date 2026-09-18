from pages.homepage import Homepage
from pages.loginpage import Login

def sort_by_price_low_to_high(driver):
    homepage = Homepage(driver)
    login = Login(driver)

    homepage.apply_sort("Price (low to high)")