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


def add_item(order: Order, name: str, quantity: int, price: int) -> None:
    order.items.append(name)
    order.quantities.append(quantity)
    order.prices.append(price)


def compute_total_price(order: Order) -> None:
    total = 0
    for i, _ in enumerate(order.items):
        total += order.quantities[i] * order.prices[i]
    print(f"The total price is: ${(total / 100):0.2f}")


def main():
    order = Order()
    add_item(order, "Keyboard", 1, 50_00)
    add_item(order, "SSD", 1, 150_00)
    add_item(order, "USB cable", 2, 5_00)

    compute_total_price(order)


if __name__ == "__main__":
    main()
