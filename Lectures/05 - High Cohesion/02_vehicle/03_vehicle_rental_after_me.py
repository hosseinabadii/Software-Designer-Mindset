PRICING = {
    "vw": {"price_per_km": 30, "price_per_day": 60_00},
    "bmw": {"price_per_km": 35, "price_per_day": 68_00},
    "ford": {"price_per_km": 35, "price_per_day": 120_00},
}


def read_brand() -> str:
    brand = ""
    while brand not in ("vw", "bmw", "ford"):
        brand = input(
            "What type of vehicle would you like to rent (choose vw, bmw, or ford)? "
        )
    return brand


def read_days() -> int:
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


def read_kw() -> int:
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


def compute_rental_price(
    days: int,
    km: int,
    price_per_day: int,
    price_per_km: int,
):
    km = max(km - 100, 0)
    return price_per_day * days + price_per_km * km


def main():
    print("Vehicle Rental before")
    brand = read_brand()
    days = read_days()
    km = read_kw()

    rental_price = compute_rental_price(
        days=days,
        km=km,
        price_per_day=PRICING[brand]["price_per_day"],
        price_per_km=PRICING[brand]["price_per_km"],
    )
    print(f"The total price of the rental is ${(rental_price / 100):.2f}")


if __name__ == "__main__":
    main()
