# SauceDemo-tests
A Pytest automation framework for the Sauce Demo application, built using Python, Selenium WebDriver, and the Page Object Model. It supports reusable page objects, test-data management, reporting, logging, failure screenshots, and parallel test execution.

## Quick Start
```bash
# Clone the repository
git clone <repo-url>
cd saucedemo-pytest-automation

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest
```
```
## Project Structure

├── pages/             # Page Object Model classes
├── tests/             # Automated test cases
├── utils/             # Common utilities and PDF helper
├── config/            # Test configuration
├── testdata/          # Checkout test data
├── reports/           # HTML execution reports
├── screenshots/       # Failure screenshots
├── order_summary/     # Generated order-summary PDF
├── conftest.py        # Pytest fixtures and hooks
├── pytest.ini         # Pytest configuration
└── requirements.txt   # Project dependencies
```
## Test Coverage

- Login with valid credentials
- Verify the inventory page
- Sort products by price: low to high
- Add the cheapest and most expensive products
- Verify the cart count
- Complete the checkout process
- Verify the order confirmation
- Generate and validate the order-summary PDF

## Running Tests
```
pytest                              # Run all tests
pytest -v                           # Run with detailed output
pytest tests/test_purchase_flow.py  # Run the purchase-flow test
pytest -n 2                         # Run tests in parallel
```
## Test Results
- HTML report: reports/report.html
- Failure screenshots: screenshots/
- Order-summary PDF: order_summary/order_summary.pdf
- Failed tests are retried automatically based on the pytest.ini configuration.