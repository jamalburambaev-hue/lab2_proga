from animal import Animal


class Parrot(Animal):

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def get_age_in_human_years(self) -> int:
        return self.get_age() * 5

    def express(self) -> None:
        print(f'{self.get_name()}: "Hello!"')
        print(r"""   \
   (o>
\\_//)
 \_/_)
  _|_
""")