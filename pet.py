from abc import ABC, abstractmethod


class Pet(ABC):
    """Интерфейс питомца. Заменяет Java-интерфейс через абстрактный класс."""

    @abstractmethod
    def express(self) -> None:
        """Показать, как питомец выражает себя."""
        ...

    @abstractmethod
    def get_name(self) -> str:
        ...

    @abstractmethod
    def get_age(self) -> int:
        ...

    @abstractmethod
    def get_age_in_human_years(self) -> int:
        ...