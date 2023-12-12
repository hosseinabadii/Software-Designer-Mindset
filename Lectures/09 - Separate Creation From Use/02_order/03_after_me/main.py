from typing import Callable

from pos.authorization import authorize_google, authorize_sms
from pos.order import Order
from pos.payment import (
    AuthorizeFunction,
    CreditPaymentProcessor,
    DebitPaymentProcessor,
    PaymentProcessor,
    PaypalPaymentProcessor,
)


def read_choice(question: str, choices: list[str]) -> str:
    choice = ""
    while choice not in choices:
        choice = input(f"{question} ({', '.join(choices)})? ")
    return choice


AUTHORIZERS: dict[str, AuthorizeFunction] = {
    "google": authorize_google,
    "sms": authorize_sms,
}


def create_paypal_processor() -> PaymentProcessor:
    email_address = input("Enter your email address: ")
    return PaypalPaymentProcessor(email_address)


def create_credit_processor() -> PaymentProcessor:
    security_code = input("Enter the security code: ")
    return CreditPaymentProcessor(security_code)


def create_debit_processor() -> PaymentProcessor:
    return DebitPaymentProcessor()


PROCESSOR_CREATOR = Callable[[], PaymentProcessor]
PROCESSORS: dict[str, PROCESSOR_CREATOR] = {
    "paypal": create_paypal_processor,
    "credit": create_credit_processor,
    "debit": create_debit_processor,
}


def create_order() -> Order:
    order = Order()
    order.add_item("Keyboard", 1, 5000)
    order.add_item("SSD", 1, 15000)
    order.add_item("USB cable", 2, 500)
    return order


def read_payment_choice() -> PaymentProcessor:
    payment_processor_choice = read_choice(
        "How would you like to pay?", list(PROCESSORS)
    )
    return PROCESSORS[payment_processor_choice]()


def read_authorizer() -> AuthorizeFunction:
    auth_choice = read_choice("Choose your authentication method", list(AUTHORIZERS))
    return AUTHORIZERS[auth_choice]


def main():
    order = create_order()
    print(f"The total price is: ${(order.total_price / 100):.2f}.")

    processor = read_payment_choice()
    authorizer = read_authorizer()
    processor.pay(order, authorizer)


if __name__ == "__main__":
    main()
