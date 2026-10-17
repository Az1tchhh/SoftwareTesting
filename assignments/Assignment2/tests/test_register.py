import re

from playwright.sync_api import Page, expect

from data.users import new_customer
from pages.register_page import RegisterPage


def test_new_customer_registration_redirects_to_login(
    page: Page, register_page: RegisterPage
) -> None:
    customer = new_customer()
    register_page.open()
    register_page.register(customer)

    expect(page).to_have_url(re.compile(r"/auth/login$"))
