# I summarized methods used in the assignment for learning purposes 

# Python Playwright cheat sheet

These are the methods used in the first test case, **register a new customer**. Add new methods here as later cases are written.

| Method | What it does here |
| --- | --- |
| `page.goto("/auth/register")` | Opens the registration page. `pytest.ini` supplies the Toolshop base URL. |
| `page.get_by_test_id("email")` | Finds the element with `data-test="email"`. `conftest.py` changes Playwright's default test ID attribute to `data-test`. |
| `locator.fill(value)` | Replaces the current input value, such as the email or password. |
| `locator.select_option("US")` | Chooses the United States option from the country `<select>`. |
| `locator.click()` | Clicks the Register button after Playwright checks that it can be clicked. |
| `expect(page).to_have_url(re.compile(r"/auth/login$"))` | Retries until the browser reaches the login page or the assertion times out. This is the test's success check. |

The `page` fixture comes from `pytest-playwright` and gives each test its own browser page and context. Our `register_page` fixture in `conftest.py` creates a page object, so the test describes the user journey while selectors stay in `pages/register_page.py`. `new_customer()` uses Python's `uuid4()` to make an email that has not been registered on an earlier run.

References: [Playwright locators](https://playwright.dev/python/docs/locators), [pytest fixtures](https://playwright.dev/python/docs/test-runners), [page assertions](https://playwright.dev/python/docs/api/class-pageassertions).

## Login and waiting for navigation

`expect(page).to_have_url(re.compile(r"/account$"))` already retries for up to its assertion timeout (5 seconds by default). It does not require a separate page-load wait. If the URL stays on `/auth/login`, check the visible error and the login request. In the saved trace, Toolshop returned HTTP 423 and displayed “Account locked, too many failed attempts.” More waiting would not unlock the account.

The login case now creates a unique customer first, then checks an unknown email and the new customer's valid credentials. `expect(login_page.error).to_be_visible()` is a retrying assertion for the rejected login. This keeps the test independent of the shared demo account's lock state.

## Reuse login for protected pages

Within **one test**, navigation on the same `page` keeps that context's login: after signing in, call `page.goto("/account/invoices")` or another route.

Across **separate tests**, pytest-playwright creates an isolated context for each test. The new `signed_in_state` fixture in `conftest.py` registers and logs in a fresh customer once per pytest session, then calls `context.storage_state()`. The `authenticated_page` fixture creates a fresh context for each protected-page test with `browser.new_context(storage_state=signed_in_state)`. Toolshop stores its token in `localStorage`, which this state captures. The state stays in memory, so no token file is written to the project.

Example for a later protected-page test:

```python
def test_account_invoices(authenticated_page: Page) -> None:
    authenticated_page.goto("/account/invoices")
    expect(authenticated_page).to_have_url(re.compile(r"/account/invoices$"))
```

Keep registration and login tests on the normal `page` fixture, because those tests need to begin signed out. A fresh context keeps browser data isolated, but tests using the same account can still affect one another through server-side changes such as orders or profile edits. [Playwright authentication guide](https://playwright.dev/python/docs/auth).

### Fixture argument names

Pytest requests a fixture by the **parameter name**. To get our authenticated page, write `def test_profile(authenticated_page: Page):`. The parameter must spell `authenticated_page` exactly; the test function can have any `test_...` name. `: Page` is an optional type hint and does not select the fixture. Writing `def test_profile(page: Page):` requests Playwright's regular signed-out `page` fixture instead. [Pytest fixture reference](https://docs.pytest.org/en/stable/reference/reference.html#fixtures).


## Compare two products

`MarketPage.first_two_product_ids()` reads two IDs from catalog cards before navigating. The test then opens each detail page, records a `ProductSnapshot(name, price)`, and adds it to the site's comparison. A `list[ProductSnapshot]` keeps each name paired with its price and preserves the order of the comparison columns. `Decimal` represents prices exactly as decimal values.

| Method | What it does here |
| --- | --- |
| `locator.nth(1).wait_for()` | Waits until the second catalog product exists. |
| `locator.get_attribute("data-test")` | Reads a card value such as `product-123`; removing the prefix gives the ID for `DetailPage.open(id)`. |
| `locator.inner_text()` | Captures the displayed name and unit price on a detail page. |
| `expect(locator).to_have_text([...])` | Retries until both comparison names or both prices match the captured list, in order. |

`self.product_name` is a Locator, so `snapshot()` calls `inner_text()` to store a string. The detail heading can include an ECO badge, which `snapshot()` removes from the captured name. The comparison page exposes `product-name` and `compare-price` cells inside `comparison-table`. [Playwright locator guide](https://playwright.dev/python/docs/locators), [Playwright assertions](https://playwright.dev/python/docs/test-assertions).

## Check stock before adding to the cart

`page.get_by_test_id("add-to-cart")` creates a Locator even when the button is absent. `locator.is_visible()` returns a boolean. `DetailPage.require_in_stock()` raises `RuntimeError` when the button is missing or hidden, so the purchase test fails with an out of stock message before trying to increase quantity.

