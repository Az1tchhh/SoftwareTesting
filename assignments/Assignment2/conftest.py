import re
from typing import Any, Iterator

import pytest
from playwright.sync_api import Browser, Page, Playwright, expect

from data.users import new_customer

from pages.register_page import RegisterPage
from pages.login_page import LoginPage

BASE_URL = "https://practicesoftwaretesting.com"

@pytest.fixture(scope="session", autouse=True)
def toolshop_test_ids(playwright: Playwright) -> None:
    playwright.selectors.set_test_id_attribute("data-test")


@pytest.fixture
def register_page(page: Page) -> RegisterPage:
    return RegisterPage(page)

@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)


@pytest.fixture(scope="session")
def signed_in_state(browser: Browser, toolshop_test_ids: None) -> dict[str, Any]:
    """Create one fresh account and keep its login state for this test session."""
    context = browser.new_context(base_url=BASE_URL)
    try:
        page = context.new_page()
        customer = new_customer()
        RegisterPage(page).open()
        RegisterPage(page).register(customer)
        expect(page).to_have_url(re.compile(r"/auth/login$"))
        LoginPage(page).login(customer.email, customer.password)
        expect(page).to_have_url(re.compile(r"/account$"))
        return context.storage_state()
    finally:
        context.close()


@pytest.fixture
def authenticated_page(browser: Browser, signed_in_state: dict[str, Any]) -> Iterator[Page]:
    """Give each protected-page test a fresh context with the saved login."""
    context = browser.new_context(base_url=BASE_URL, storage_state=signed_in_state)
    try:
        yield context.new_page()
    finally:
        context.close()
