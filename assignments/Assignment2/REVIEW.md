## AI changes

AI initially helped me set up the Python Playwright project and write the registration test. It added a reusable page object, pytest fixtures, unique customer data, and a Playwright cheat sheet. The Python files were checked for syntax errors, but the assistant did not run the browser test.

## How did I review the AI output?

After the registration test was created, I ran it with tracing enabled:

```bash
pytest --tracing on
```

The trace let me inspect the steps performed during the test. I also reviewed the code structure and found no unnecessary code. I used this style as a baseline and wrote the next two test cases myself.

## Problem with account locking

Repeated login attempts with the same account caused it to be locked. At first, I could not tell why login was failing, so I asked the AI assistant for help. It suggested registering a new account, checking that invalid credentials are rejected, and then logging in with the new account's valid credentials. This let me check both login flows without relying on a shared account that might already be locked.

## Reusing authentication across tests

I did not want to log in again at the start of every test that needs an authenticated user. The AI assistant helped me add a session-scoped fixture that creates an account, logs in, and saves its authentication state. The `authenticated_page` fixture then gives each test a fresh browser context loaded with that state.

## Selecting and comparing multiple products

I asked the AI assistant for help with test case 4 because selecting and tracking two products in the HTML was difficult. It suggested capturing each product's name and price together and checking those values against the site's comparison table. The first version navigated using product links. I changed it to extract product IDs from the catalog cards and reuse `DetailPage.open(id)` to open each product.

## Out of stock
Product can go out of stock... Need to assert some things in a buying process. Added if statement whether "Out of stock" shown or not. If yes, then will raise an exception in Runtime