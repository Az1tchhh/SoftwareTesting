from dataclasses import dataclass
from uuid import uuid4


@dataclass(frozen=True)
class Customer:
    first_name: str
    last_name: str
    email: str
    password: str


def new_customer() -> Customer:
    return Customer(
        first_name="Test",
        last_name="Customer",
        email=f"toolshop-{uuid4().hex}@example.com",
        password="TestCustomer#2026",
    )

def existing_customer() -> Customer:
    return Customer(
        first_name="Test",
        last_name="Customer",
        email=f"customer@practicesoftwaretesting.com",
        password="welcome01",
    )