import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.config_loader import load_config
from pages.loginpage import Login
from utils.screenshot_utils import ScreenshotUtil
from utils.user_data_loader import get_user


def pytest_addoption(parser):
    """Add command-line options for browser execution."""

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


def create_driver(browser_name, headless):
    """Create and configure a WebDriver instance."""

    if browser_name == "chrome":
        options = ChromeOptions()

        # Disable Chrome password manager and password breach popup
        options.add_experimental_option(
            "prefs",
            {
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False,
                "profile.password_manager_leak_detection": False,
            },
        )

        options.add_argument(
            "--disable-features="
            "PasswordLeakDetection,PasswordManagerOnboarding"
        )
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--window-size=1920,1080")
        else:
            options.add_argument("--start-maximized")

        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()

        if headless:
            options.add_argument("--headless")

        browser = webdriver.Firefox(options=options)

        if headless:
            browser.set_window_size(1920, 1080)
        else:
            browser.maximize_window()

    else:
        raise ValueError(
            f"Unsupported browser: {browser_name}"
        )

    browser.set_page_load_timeout(30)
    browser.set_script_timeout(30)

    return browser


@pytest.fixture(scope="function")
def driver(request):
    """
    Create a fresh browser session for every test and terminate it
    after the test finishes.
    """

    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    browser = create_driver(browser_name, headless)

    yield browser

    browser.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    """Open SauceDemo and log in before executing a test."""

    driver.get("https://www.saucedemo.com/")

    user = get_user()

    if not user["username"] or not user["password"]:
        pytest.fail(
            "SauceDemo credentials are missing from the .env file."
        )

    login_page = Login(driver)
    login_page.login(
        user["username"],
        user["password"],
    )

    return driver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture a screenshot after every test execution."""

    outcome = yield
    report = outcome.get_result()

    if report.when != "call":
        return

    browser = item.funcargs.get("driver")

    if browser:
        ScreenshotUtil.save_screenshot(
            browser,
            name_prefix=f"{item.name}_{report.outcome}",
        )

@pytest.fixture(scope="session")
def base_url():
    """Return the SauceDemo application URL from config.yaml"""

    config = load_config()
    url = config.get("base_url")

    if not url:
        pytest.fail(
            "The 'base_url' value is missing from config.yaml."
        )
    return url