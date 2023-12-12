from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    OPEN = "open"
    PAID = "paid"


@dataclass
class Item:
    name: str
    quantity: int
    price: int


class Order:
    def __init__(self):
        self.items: list[Item] = []
        self.status: Status = Status.OPEN

    def add_item(self, item: Item) -> None:
        self.items.append(item)


class DebitPayment:
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing debit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = Status.PAID


class CreditPayment:
    def pay(self, order: Order, security_code: str) -> None:
        print("Processing credit payment type")
        print(f"Verifying security code: {security_code}")
        order.status = Status.PAID


def main() -> None:
    order = Order()
    order.add_item(Item(name="Keyboard", quantity=1, price=50_00))
    order.add_item(Item(name="SSD", quantity=1, price=150_00))
    order.add_item(Item(name="USB cable", quantity=2, price=5_00))
    print(order.status)

    payment = DebitPayment()
    payment.pay(order, security_code="0372846")
    print(order.status)


if __name__ == "__main__":
    main()
