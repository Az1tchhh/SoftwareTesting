from playwright.sync_api import Page, expect

from data.products import ProductSnapshot
from pages.compare_page import ComparePage
from pages.detail_page import DetailPage
from pages.market_page import MarketPage


def test_comparison_shows_two_products_names_and_prices(page: Page) -> None:
    market = MarketPage(page)
    detail = DetailPage(page)
    comparison = ComparePage(page)

    market.open()
    product_ids = market.first_two_product_ids()
    snapshots: list[ProductSnapshot] = []

    for product_id in product_ids:
        detail.open(product_id)
        snapshots.append(detail.snapshot())
        detail.add_to_comparison()

    detail.open_comparison()
    expect(comparison.table).to_be_visible()
    expect(comparison.names).to_have_text([item.name for item in snapshots])
    expect(comparison.prices).to_have_text(
        [f"${item.price:.2f}" for item in snapshots]
    )
