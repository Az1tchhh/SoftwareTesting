import re

from playwright.sync_api import Page, expect

from data.users import new_customer
from pages.forgot_password_page import ForgotPasswordPage
from pages.register_page import RegisterPage


def test_reset_password_request(page: Page, register_page: RegisterPage) -> None:
    customer = new_customer()
    register_page.open()
    register_page.register(customer)
    expect(page).to_have_url(re.compile(r"/auth/login$"))

    forgot_password = ForgotPasswordPage(page)
    forgot_password.open_from_login()
    expect(page).to_have_url(re.compile(r"/auth/forgot-password$"))

    unknown_response = forgot_password.request_reset(f"123{customer.email}")
    assert unknown_response.status == 422, unknown_response.text()

    known_response = forgot_password.request_reset(customer.email)
    assert known_response.ok, known_response.text()
    expect(forgot_password.confirmation).to_be_visible()
