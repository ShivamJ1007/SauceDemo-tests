from pages.loginpage import Login
from pages.checkout_page import CheckoutPage
from pages.inventorypage import InventoryPage
from pages.cart_page import CartPage
from utils.user_data_loader import get_user
from utils.pdf_util import PDFUtil
from pathlib import Path


def test_checkout(driver, base_url):
    login = Login(driver)
    checkout_page = CheckoutPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    user = get_user()

    driver.get(base_url)
    login.login(user["username"],user["password"])
    inventory_page.apply_sort("Price (low to high)")
    inventory_page.add_cheapest_and_most_expensive()
    inventory_page.driver.find_element(*inventory_page.CART).click()

    assert cart_page.get_cart_item_count() == 2

    cart_page.driver.find_element(*cart_page.CHECKOUT_BUTTON).click()

    assert checkout_page.driver.find_element(*checkout_page.PAGE_TITLE).is_displayed(), "Checkout information page is not displayed"

    checkout_page.enter_checkout_information(
        first_name="Shivam",
        last_name="Sharma",
        postal_code="110001"
    )

    checkout_page.driver.find_element(*checkout_page.CONTINUE_BUTTON).click()

    assert checkout_page.get_page_title() == "Checkout: Overview", (
        "Checkout overview page is not displayed"
    )
    overview_products = checkout_page.get_overview_product_names()
    overview_prices = checkout_page.get_overview_product_prices()

    assert len(overview_products) == 2, (
        f"Expected 2 products, but found {len(overview_products)}"
    )

    assert len(overview_prices) == 2, (
        f"Expected 2 prices, but found {len(overview_prices)}"
    )

    item_total = checkout_page.get_item_total()
    tax = checkout_page.get_tax()
    final_total = checkout_page.get_final_total()

    assert "Item total:" in item_total
    assert "Tax:" in tax
    assert "Total:" in final_total

    checkout_page.click_finish()

    assert checkout_page.get_page_title() == "Checkout: Complete!", (
        "Order confirmation page is not displayed"
    )

    assert "Thank you for your order!" in (
        checkout_page.get_confirmation_text()
        )

    assert "Your order has been dispatched" in (
        checkout_page.get_confirmation_text()
    )

    pdf_path = "order_summary/order_summary.pdf"

    PDFUtil.generate_order_summary(
        file_path=pdf_path,
        customer_name="Shivam Sharma",
        product_names=overview_products,
        product_prices=overview_prices,
        item_total=item_total,
        tax=tax,
        final_total=final_total,
        order_status=checkout_page.get_confirmation_text(),
    )

    # Verify that the PDF was created
    assert Path(pdf_path).exists(), (
        f"Order-summary PDF was not created at {pdf_path}"
    )

    # Verify that the PDF is not empty
    assert Path(pdf_path).stat().st_size > 0, (
        "Generated order-summary PDF is empty"
    )

    # Read the generated PDF
    pdf_text = PDFUtil.read_pdf(pdf_path)

    # Validate PDF details
    assert "SauceDemo Order Summary" in pdf_text
    assert "Shivam Sharma" in pdf_text

    for product_name in overview_products:
        assert product_name in pdf_text

    for product_price in overview_prices:
        assert product_price in pdf_text

    assert item_total in pdf_text
    assert tax in pdf_text
    assert final_total in pdf_text
    assert "Thank you for your order!" in pdf_text
