from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


class FuelType(Enum):
    PETROL = auto()
    DIESEL = auto()
    ELECTRIC = auto()


@dataclass
class Vehicle:
    brand: str
    model: str
    color: str
    fuel_type: FuelType
    licencse_plate: str
    price_per_km: int
    price_per_day: int
    reserved: bool

    def total_price(self, days: int, additional_km: int) -> int:
        return self.price_per_km * additional_km + self.price_per_day * days


class ContractStatus(Enum):
    ORDERED = auto()
    PAID = auto()
    PICKED_UP = auto()
    DROPPED_OFF = auto()
    CANCELLED = auto()


@dataclass
class Customer:
    id: int
    name: str
    address: str
    postal_code: str
    city: str
    email: str


@dataclass
class RentalContract:
    vehicle: Vehicle
    customer: Customer
    contract_status: ContractStatus
    pickup_date: datetime
    days: int = 1
    additional_km: int = 0

    @property
    def total_price(self) -> int:
        return self.vehicle.total_price(self.days, self.additional_km)


def read_vehicle_type(vehicle_types: list[str]) -> str:
    """Reads the vehicle type from the user."""
    vehicle_type = ""
    while vehicle_type not in vehicle_types:
        vehicle_type = input(
            f"What type of vehicle would you like to rent {vehicle_types}? "
        )
    return vehicle_type


def read_rent_days() -> int:
    """Reads the number of days from the user."""
    days = 0
    while days < 1:
        days_str = input(
            "How many days would you like to rent the vehicle? (enter a positive number) "
        )
        try:
            days = int(days_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return days


def read_kms_to_drive() -> int:
    """Reads the number of kilometers to drive from the user."""
    km = 0
    while km < 1:
        km_str = input(
            "How many kilometers would you like to drive (enter a positive number)? "
        )
        try:
            km = int(km_str)
        except ValueError:
            print("Invalid input. Please enter a number.")
    return km


def main():
    FREE_KMS = 100
    VEHICLES = {
        "vw": Vehicle(
            "volkswagen", "Golf", "black", FuelType.PETROL, "ABC123", 30, 6000, False
        ),
        "bmw": Vehicle(
            "BMW", "XS", "green", FuelType.PETROL, "ABC123", 30, 8500, False
        ),
        "ford": Vehicle(
            "Ford", "Fiesta", "white", FuelType.PETROL, "ABC123", 30, 12000, False
        ),
    }

    vehicle_type = read_vehicle_type(list(VEHICLES.keys()))
    days = read_rent_days()
    additional_km = read_kms_to_drive()

    customer = Customer(
        id=12345,
        name="My name",
        address="Some address",
        postal_code="1234",
        city="Some city",
        email="abc@abc.com",
    )

    rental = RentalContract(
        vehicle=VEHICLES[vehicle_type],
        customer=customer,
        contract_status=ContractStatus.ORDERED,
        pickup_date=datetime.now(),
        days=days,
        additional_km=max(additional_km - FREE_KMS, 0),
    )
    print(rental)
    print(f"The total price of the rental is ${(rental.total_price / 100):.2f}")


if __name__ == "__main__":
    main()
