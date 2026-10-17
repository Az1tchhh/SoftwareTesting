# AI model for assistance
GPT-6-sol with medium effort. Good for coding and has a good context size by default.

# Prompt log

1. “Can you everytime I prompt you, write the prompt in PROMPT.md? include last message and at the end just explain in text what is being done by your change”

2. “Add last 2 prompts”

3. “I wrote DESCRIPTION.md file with a aim of the project. We have to test this site with given 5 test cases. Do one at a time then compile. I will make corrections after if necessary. I would appreciate you if you will guide me with library methods while you write tests and save them like in some cheat sheet in different file”

4. “I am having issue in Assertion at expect(page).to_have_url(re.compile(r"/account$")). I guess it doesnt wait for page to load up.”

The saved login trace shows that Toolshop returned HTTP 423 because the shared customer account was locked; the URL assertion was already waiting correctly. This change makes the login test create a fresh customer and check both rejected and valid credentials. It also explains the assertion in the cheat sheet. The changed Python files were compiled, and no browser test was run by the assistant.

5. “How can I check pages consequently without needing to authorize in each testing?”

This change adds session-scoped login state and an `authenticated_page` fixture for later protected-page tests. Each such test gets a fresh browser context loaded with the same login state, while registration and login tests remain signed out. The cheat sheet explains both navigation within one test and state reuse across tests. The Python fixture was compiled; no browser test was run.

6. “So in order to use authenticated_page fixture, it needs to be passed as an arugment of a function with 1to1 characters?”

This change explains that pytest injects fixtures by exact parameter name. The cheat sheet now shows that `authenticated_page` requests the signed-in fixture, `page` requests the regular fixture, and the `Page` type hint is optional. No test code or browser behavior changed.

7. “How can I make a comparison of two products? 4-test case. How to track name and price of multiple objects?”

This change records the question about test case 4. The suggested approach is to capture each product's name and price together in a product snapshot, then compare both snapshots with the site's comparison table. No comparison test code was written or run.

8. “Maybe instead of links, we will get ids, and just open details with open(id)?”

This change switches case 4 from catalog links to product IDs read from each card's `data-test` attribute. It reuses `DetailPage.open(id)` and removes the redundant link-opening method.

9. “Yes, do it. And why dont we use just name = self.product_name in snapshot()?”

This change completes the ID-based navigation and explains in the cheat sheet that `self.product_name` is a Playwright Locator; `inner_text()` reads the string needed by `ProductSnapshot`. The Python files were compiled, and pytest was not run.

10. “Can you refine my text in REVIEW.md?”

This change improves the grammar and clarity of `REVIEW.md` while keeping its five-section structure and first-person account. It clarifies how tracing was used, how the login fixtures share authentication state, and how product IDs are used in the comparison test. No test code was changed or run.

12. “My code that i have written falls at tests/test_buy_product.py:42: AssertionError? why?”

This review explains that the payment success message confirms payment validation, while the order confirmation appears only after a separate invoice creation request succeeds. The site's invoice error handler does not display failures, so the invoice response or a trace is needed to identify the exact cause. No test code was changed or run.

13. “is it correct that I took page.locator("#order-confirmation") when it is div with id="order-confirmation"?”

This explanation confirms that `#order-confirmation` is the CSS ID selector for the div. The locator is valid; the failed visibility assertion means the confirmation did not appear within the wait period. No test code was changed or run.

14. “It works when i run with webkit, but fails when i run with pytest. Why?”

This review found that plain pytest defaults to Chromium while the successful command selected WebKit. The pytest failure cache identifies the purchase case on Chromium. The exact checkout failure still needs a Chromium trace or invoice response; no test code was changed or run.

