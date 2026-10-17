## 2-ASSIGNMENT
Instead of using TypeScript as a mother-language for PlayWright, I chose python as it is my main language in every day life. 

I am using https://playwright.dev/python/docs/intro as a main source of documentation.

## After cloning
Install pytest-playwright plugin in your end device using pip

```bash
pip install pytest-playwright
```

After that simply run following command in console at location ./Assignment2:

```bash
pytest
```

## PAGE TO TEST
https://practicesoftwaretesting.com

## TEST CASES
1. **Register a new customer**
   Test that a unique new account is created and the user ends up signed in or on the login page

2. **Log in**
   Test that valid credentials reach the account page; invalid ones show the error and do not

3. **Buy a product**
   Test that adding a product to the cart shows the right item and quantity, and that checkout completes.

4. **Compare two products**
   Open two products, capture name and price, assert the comparison you state

5. **Reset a password**
   Test that the forgot-password flow gives the expected confirmation for a known email, and an error for an invalid one


## REQUIREMENTS
1. At least one fixture.
2. Every test has an assertion that could fail.
