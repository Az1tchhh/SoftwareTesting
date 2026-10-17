from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_title = page.get_by_test_id("product-title")
        self.product_quantity = page.get_by_test_id("product-quantity")
        self.product_price = page.get_by_test_id("product-price")

    def open(self) -> None:
        self.page.get_by_test_id("nav-cart").click()

    def proceed(self) -> None:
        self.page.get_by_test_id("proceed-1").click()
