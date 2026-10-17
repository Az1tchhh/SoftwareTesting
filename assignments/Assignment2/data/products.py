from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Product:
    name: str


@dataclass
class CartProduct:
    name: str
    quantity: int
    price: float


@dataclass(frozen=True)
class ProductSnapshot:
    name: str
    price: Decimal


def existing_product() -> Product:
    return Product(name="Cordless Drill 20V")
