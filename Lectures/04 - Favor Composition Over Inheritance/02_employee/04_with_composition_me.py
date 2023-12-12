"""
Very advanced Employee management system.
"""

from dataclasses import dataclass, field
from typing import Protocol


class Payment(Protocol):
    def compute_pay(self) -> int:
        ...


@dataclass
class HourlyPayment:
    pay_rate: int = 50_00
    hours_worked: float = 0.0
    employer_cost: int = 1000_00

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked + self.employer_cost)


@dataclass
class MonthlyPayment:
    monthly_salary: int = 0
    percentage: float = 1.0

    def compute_pay(self) -> int:
        return int(self.monthly_salary * self.percentage)


@dataclass
class ContractLandedPayment:
    commission: int = 100_00
    contracts_landed: int = 0

    def compute_pay(self) -> int:
        return self.commission * self.contracts_landed


@dataclass
class FreelancerPayment:
    pay_rate: int = 50_00
    hours_worked: float = 0

    def compute_pay(self) -> int:
        return int(self.pay_rate * self.hours_worked)


@dataclass
class Employee:
    name: str
    id: int
    payments: list[Payment] = field(default_factory=list)

    def add_payment(self, payment: Payment) -> None:
        self.payments.append(payment)

    def compute_pay(self):
        return sum(payment.compute_pay() for payment in self.payments)


def main() -> None:
    henry = Employee(name="Henry", id=12346)
    henry.add_payment(HourlyPayment(pay_rate=50_00, hours_worked=100))
    henry.add_payment(ContractLandedPayment(contracts_landed=1))

    sarah = Employee(name="Sarah", id=47832)
    sarah.add_payment(MonthlyPayment(monthly_salary=5000_00))
    sarah.add_payment(ContractLandedPayment(contracts_landed=12))

    david = Employee(name="David", id=99999)
    david.add_payment(FreelancerPayment(pay_rate=30_00, hours_worked=50))
    david.add_payment(ContractLandedPayment(contracts_landed=3))

    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")
    print(f"{david.name} earned ${(david.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
