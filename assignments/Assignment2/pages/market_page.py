from playwright.sync_api import Page

from data.products import Product


class MarketPage:
    def __init__(self, page: Page) -> None:
        self.page = page

    def open(self) -> None:
        self.page.goto("/")

    def product_detail_open(self, product: Product) -> None:
        self.page.get_by_test_id("search-query").fill(product.name)
        self.page.get_by_test_id("search-submit").click()
        self.page.locator('a[data-test^="product-"]').filter(
            has_text=product.name
        ).click()

    def first_two_product_ids(self) -> tuple[str, str]:
        cards = self.page.locator('a[data-test^="product-"]')
        cards.nth(1).wait_for()
        product_ids = []
        for index in range(2):
            test_id = cards.nth(index).get_attribute("data-test")
            product_id = test_id.removeprefix("product-")
            product_ids.append(product_id)
        return product_ids[0], product_ids[-1]
