from playwright.sync_api import Page

from data.users import Customer


class RegisterPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto("/auth/register")

    def register(self, customer: Customer) -> None:
        self.page.get_by_test_id("first-name").fill(customer.first_name)
        self.page.get_by_test_id("last-name").fill(customer.last_name)
        self.page.get_by_test_id("dob").fill("1995-05-20")
        self.page.get_by_test_id("country").select_option("US")
        self.page.get_by_test_id("postal_code").fill("90210")
        self.page.get_by_test_id("house_number").fill("12")
        self.page.get_by_test_id("street").fill("Main Street")
        self.page.get_by_test_id("city").fill("Beverly Hills")
        self.page.get_by_test_id("state").fill("California")
        self.page.get_by_test_id("phone").fill("15551234567")
        self.page.get_by_test_id("email").fill(customer.email)
        self.page.get_by_test_id("password").fill(customer.password)
        self.page.get_by_test_id("register-submit").click()
