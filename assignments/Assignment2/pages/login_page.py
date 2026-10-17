from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.error = page.get_by_test_id("login-error")

    def open(self) -> None:
        self.page.goto("/auth/login")

    def login(self, email: str, password: str) -> None:
        self.page.get_by_test_id("email").fill(email)
        self.page.get_by_test_id("password").fill(password)
        self.page.get_by_test_id("login-submit").click()
