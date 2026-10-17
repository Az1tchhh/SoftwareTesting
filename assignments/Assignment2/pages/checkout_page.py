from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.payment_success = page.get_by_test_id("payment-success-message")
        self.order_confirmation = page.locator("#order-confirmation")

    def proceed_as_signed_in_customer(self) -> None:
        self.page.get_by_test_id("proceed-2").click()

    def enter_address(self) -> None:
        self.page.get_by_test_id("country").select_option("Kazakhstan")
        self.page.get_by_test_id("postal_code").fill("050042")
        self.page.get_by_test_id("house_number").fill("20")
        self.page.get_by_test_id("street").fill("taugul-1")
        self.page.get_by_test_id("city").fill("Almaty")
        self.page.get_by_test_id("state").fill("Almaty")
        self.page.get_by_test_id("proceed-3").click()

    def choose_cash_on_delivery(self) -> None:
        self.page.get_by_test_id("payment-method").select_option("cash-on-delivery")

    def confirm_payment(self) -> None:
        self.page.get_by_test_id("finish").click()

    def place_order(self) -> None:
        self.page.get_by_test_id("finish").click()
