import re

from playwright.sync_api import Page, expect

from data.users import new_customer
from pages.login_page import LoginPage
from pages.register_page import RegisterPage


def test_customer_login(
    page: Page,
    login_page: LoginPage,
    register_page: RegisterPage,
) -> None:
    customer = new_customer()
    register_page.open()
    register_page.register(customer)
    expect(page).to_have_url(re.compile(r"/auth/login$"))

    login_page.login(f"unknown-{customer.email}", customer.password)
    expect(login_page.error).to_be_visible()
    expect(page).to_have_url(re.compile(r"/auth/login$"))

    login_page.login(customer.email, customer.password)
    expect(page).to_have_url(re.compile(r"/account$"))
