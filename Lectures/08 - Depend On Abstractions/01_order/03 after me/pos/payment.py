from abc import ABC, abstractmethod
from typing import Callable, Protocol

from pos.data import PaymentStatus

Authorizer = Callable[[], bool]


class Payable(Protocol):
    def set_payment_status(self, status: PaymentStatus) -> None:
        ...

    @property
    def total_price(self) -> int:
        ...


class PaymentProcessor(ABC):
    def authorize(self, authorizer: Authorizer) -> None:
        if not authorizer():
            raise Exception("Not authorized")

    @abstractmethod
    def pay(self, payable: Payable) -> None:
        pass


class DebitPaymentProcessor(PaymentProcessor):
    def pay(self, payable: Payable) -> None:
        print(f"Processing debit payment for amount: ${(payable.total_price / 100):.2f}.")
        payable.set_payment_status(PaymentStatus.PAID)


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code: str) -> None:
        self.security_code = security_code

    def pay(self, payable: Payable) -> None:
        print(
            f"Processing credit payment for amount: ${(payable.total_price / 100):.2f}."
        )
        print(f"Verifying security code: {self.security_code}")
        payable.set_payment_status(PaymentStatus.PAID)


class PayPalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address: str) -> None:
        self.email_address = email_address

    def pay(self, payable: Payable) -> None:
        print(
            f"Processing PayPal payment for amount: ${(payable.total_price / 100):.2f}."
        )
        print(f"Using email address: {self.email_address}")
        payable.set_payment_status(PaymentStatus.PAID)
