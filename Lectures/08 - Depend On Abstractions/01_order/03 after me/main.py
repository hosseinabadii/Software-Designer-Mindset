from pos.authorization import authorize_sms
from pos.order import Order
from pos.payment import DebitPaymentProcessor


def main():
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)
    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    processor = DebitPaymentProcessor()
    processor.authorize(authorize_sms)
    processor.pay(order)


if __name__ == "__main__":
    main()
