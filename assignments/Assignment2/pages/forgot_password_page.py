from playwright.sync_api import Page, Response


class ForgotPasswordPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.form = page.get_by_test_id("forgot-password-form")
        self.error = self.form.locator(".alert-danger")
        self.confirmation = self.form.locator(".alert-success")

    def open_from_login(self) -> None:
        self.page.get_by_test_id("forgot-password-link").click()

    def request_reset(self, email: str) -> Response:
        with self.page.expect_response(
            lambda response: response.request.method == "POST"
            and response.url.rstrip("/").endswith("/users/forgot-password")
        ) as response_info:
            self.form.get_by_test_id("email").fill(email)
            self.form.get_by_test_id("forgot-password-submit").click()
        return response_info.value
