from enum import Enum, auto


class PaymentStatus(Enum):
    """Payment status"""

    OPEN = auto()
    PAID = auto()


class Order:
    def __init__(self):
        self.items: list[str] = []
        self.quantities: list[int] = []
        self.prices: list[int] = []
        self.status: PaymentStatus = PaymentStatus.OPEN

    def add_item(self, name: str, quantity: int, price: int) -> None:
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    @property
    def total_price(self) -> int:
        total = 0
        for i, _ in enumerate(self.items):
            total += self.quantities[i] * self.prices[i]
        return total


def main():
    order = Order()
    order.add_item("Keyboard", 1, 50_00)
    order.add_item("SSD", 1, 150_00)
    order.add_item("USB cable", 2, 5_00)

    print(f"The total price is: ${(order.total_price / 100):0.2f}")


if __name__ == "__main__":
    main()
