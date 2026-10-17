from playwright.sync_api import Page


class ComparePage:
    def __init__(self, page: Page) -> None:
        self.table = page.get_by_test_id("comparison-table")
        self.names = self.table.get_by_test_id("product-name")
        self.prices = self.table.get_by_test_id("compare-price")
