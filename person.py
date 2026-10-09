from typing import Optional
from pet import Pet

class Person:

    def __init__(self, name: str, pet: Optional[Pet] = None) -> None:
        self._name = name
        self._pet: Optional[Pet] = pet

    def set_pet(self, pet: Optional[Pet]) -> None:
        self._pet = pet

    def get_pet_info(self) -> None:
        print("-" * 20)
        if self._pet is None:
            print(f"{self._name} has no pet yet")
            print("-" * 20)
            return

        print(f"Pet for {self._name} is named {self._pet.get_name()}")
        print(
            f"Age: {self._pet.get_age()} year(s), "
            f"about {self._pet.get_age_in_human_years()} human years"
        )
        print("And it expresses itself like this:")
        self._pet.express()
        print("-" * 20)