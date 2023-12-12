from dataclasses import dataclass
from typing import Protocol


class BaseUser(Protocol):
    def change_name(self, value: str) -> None:
        ...

@dataclass
class User:
    name: str
    age: int

    def change_name(self, value: str) -> None:
        self.name = value

    def get_age(self):
        return self.age


@dataclass
class FakeUser:
    name: str
    age: int

    def get_age(self):
        return self.age

    def change_name(self, value: str) -> None:
        self.name = "Fake " + value


def make_default(user: BaseUser):
    user.change_name("Default")


if __name__ == "__main__":
    user = User("Ali", 20)
    print(user)
    make_default(user)
    print(user)

    fake_user = FakeUser("Ali", 20)
    print(fake_user)
    make_default(fake_user)
    print(fake_user)
