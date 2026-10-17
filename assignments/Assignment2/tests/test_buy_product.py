from playwright.sync_api import Page, expect

from data.products import CartProduct, existing_product
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.detail_page import DetailPage
from pages.market_page import MarketPage


def test_buy_product(authenticated_page: Page) -> None:
    product = existing_product()
    market = MarketPage(authenticated_page)
    detail = DetailPage(authenticated_page)
    cart = CartPage(authenticated_page)
    checkout = CheckoutPage(authenticated_page)

    market.open()
    market.product_detail_open(product)
    expect(detail.product_name).to_contain_text(product.name)
    detail.require_in_stock()

    cart_product = CartProduct(
        name=product.name,
        quantity=1,
        price=float(detail.unit_price.inner_text()),
    )
    detail.product_add_quantity(cart_product)
    expect(detail.quantity).to_have_value(str(cart_product.quantity))
    detail.add_to_cart()

    cart.open()
    expect(cart.product_title).to_have_text(cart_product.name)
    expect(cart.product_quantity).to_have_value(str(cart_product.quantity))
    expect(cart.product_price).to_have_text(f"${cart_product.price:.2f}")

    cart.proceed()
    checkout.proceed_as_signed_in_customer()
    checkout.enter_address()
    checkout.choose_cash_on_delivery()
    checkout.confirm_payment()
    expect(checkout.payment_success).to_be_visible()
