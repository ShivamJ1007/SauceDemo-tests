import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


def pytest_addoption(parser):
    """Add command-line options for browser configuration."""

    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=["chrome", "firefox"],
        help="Browser to run tests on: chrome or firefox",
    )

    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run the browser in headless mode",
    )


def create_driver(browser, headless):
    """Create and configure the WebDriver instance."""

    if browser == "chrome":
        options = ChromeOptions()

        if headless:
            options.add_argument("--headless=new")

        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(options=options)

    elif browser == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        driver = webdriver.Firefox(options=options)
        driver.maximize_window()

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)

    return driver


@pytest.fixture(scope="function")
def driver(request):
    """
    Create a fresh WebDriver instance for every test and close it
    after the test execution.
    """

    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    web_driver = create_driver(browser, headless)

    yield web_driver

    if web_driver:
        web_driver.quit()