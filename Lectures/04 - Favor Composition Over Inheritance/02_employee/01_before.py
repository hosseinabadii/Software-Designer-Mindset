"""
Very advanced Employee management system.
"""

from dataclasses import dataclass


@dataclass
class HourlyEmployee:
    name: str
    id: int
    commission: int = 10000
    contracts_landed: float = 0

    pay_rate: int = 0
    hours_worked: float = 0
    employer_cost: int = 1000_00

    def compute_pay(self) -> int:
        return int(
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )


@dataclass
class SalariedEmployee:
    name: str
    id: int
    commission: int = 10000
    contracts_landed: float = 0

    monthly_salary: int = 0
    percentage: float = 1

    def compute_pay(self) -> int:
        return int(
            self.monthly_salary * self.percentage
            + self.commission * self.contracts_landed
        )


@dataclass
class Freelancer:
    name: str
    id: int
    commission: int = 100_00
    contracts_landed: float = 0

    pay_rate: int = 0
    hours_worked: float = 0
    vat_number: str = ""

    def compute_pay(self) -> int:
        return int(
            self.pay_rate * self.hours_worked + self.commission * self.contracts_landed
        )


def main() -> None:
    henry = HourlyEmployee(
        name="Henry", id=12346, contracts_landed=1, pay_rate=50_00, hours_worked=100
    )
    sarah = SalariedEmployee(
        name="Sarah", id=47832, contracts_landed=12, monthly_salary=5000_00
    )
    david = Freelancer(
        name="David", id=99999, contracts_landed=3, pay_rate=30_00, hours_worked=50
    )

    print(f"{henry.name} earned ${(henry.compute_pay() / 100):.2f}.")
    print(f"{sarah.name} earned ${(sarah.compute_pay() / 100):.2f}.")
    print(f"{david.name} earned ${(david.compute_pay() / 100):.2f}.")


if __name__ == "__main__":
    main()
