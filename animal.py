from pet import Pet


class Animal(Pet):
    """Абстрактное животное. Реализует общее состояние и поведение."""

    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    def happy_birthday(self) -> None:
        self._age += 1

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age