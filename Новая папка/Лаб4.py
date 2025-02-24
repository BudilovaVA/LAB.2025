if __name__ == "__main__":
    class Animal:
        """
        Базовый класс для всех животных.
        """

        def __init__(self, name: str, age: int) -> None:

            self.__name = name  # Название животного (приватный атрибут)
            self.__age = age  # Возраст животного (приватный атрибут)

        def speak(self) -> str:
            """
            :return: Звук животного
            """
            return "Some sound"

        def __str__(self) -> str:
            """
            Возвращает строковое представление животного.
            :return: Строка с именем и возрастом животного.
            """
            return f"{self.__name}, возраст: {self.__age} года(лет)"

        def __repr__(self) -> str:
            """
            Возвращает явное представление животного для отладки.
            :return: Строка, содержащая имя и возраст.
            """
            return f"Animal(name={self.__name}, age={self.__age})"


    class Dog(Animal):
        """
        Класс для собак, наследуется от Animal.
        """

        def __init__(self, name: str, age: int, breed: str) -> None:
            """
            :param name: Имя собаки
            :param age: Возраст собаки
            :param breed: Порода собаки
            """
            super().__init__(name, age)
            self.breed = breed

        def speak(self) -> str:
            """
            :return: Звук собаки
            """
            return "Гав!"

        def __str__(self) -> str:
            """
            Возвращает строковое представление собаки.
            :return: Строка с именем, возрастом и породой собаки.
            """
            return f"{super().__str__()}, порода: {self.breed}"


    class Cat(Animal):
        """
        Класс для кошек, наследуется от Animal.
        """

        def __init__(self, name: str, age: int, color: str) -> None:
            """
            :param name: Имя кошки
            :param age: Возраст кошки
            :param color: Цвет шерсти кошки
            """
            super().__init__(name, age)
            self.color = color

        def speak(self) -> str:
            """
            :return: Звук кошки
            """
            return "Мяу!"

        def __str__(self) -> str:
            """
            Возвращает строковое представление кошки.
            :return: Строка с именем, возрастом и цветом кошки.
            """
            return f"{super().__str__()}, цвет: {self.color}"


    if __name__ == "__main__":
        dog = Dog("Бобик", 5, "Такса")
        cat = Cat("Мурка", 3, "Белая")
        print(dog)
        print(cat)
        print(dog.speak())
        print(cat.speak())
    pass
