from playwright.sync_api import Page

from decimal import Decimal

from data.products import CartProduct, ProductSnapshot


class DetailPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.product_name = page.get_by_test_id("product-name")
        self.unit_price = page.get_by_test_id("unit-price")
        self.quantity = page.get_by_test_id("quantity")

    def open(self, product_id: str) -> None:
        self.page.goto(f"/product/{product_id}")

    def require_in_stock(self) -> None:
        if self.page.get_by_test_id("out-of-stock").is_visible():
            raise RuntimeError("Product is out of stock: Add to cart button is missing")

    def product_add_quantity(self, cart_product: CartProduct) -> None:
        self.page.get_by_test_id("increase-quantity").click()
        cart_product.quantity += 1

    def product_reduce_quantity(self, cart_product: CartProduct) -> None:
        self.page.get_by_test_id("decrease-quantity").click()
        cart_product.quantity -= 1

    def add_to_cart(self) -> None:
        self.page.get_by_test_id("add-to-cart").click()

    def snapshot(self) -> ProductSnapshot:
        name = self.product_name.inner_text().strip().removesuffix("ECO").strip()
        return ProductSnapshot(
            name=name,
            price=Decimal(self.unit_price.inner_text().strip()),
        )

    def add_to_comparison(self) -> None:
        self.page.get_by_test_id("add-to-compare").click()

    def open_comparison(self) -> None:
        self.page.get_by_test_id("compare-link").click()
