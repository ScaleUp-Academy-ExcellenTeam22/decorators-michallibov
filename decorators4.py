from abc import abstractmethod


class Animal:
    """
    This class is the base class for all animals. It contains
    property and abstract decorators.
    """
    def __init__(self, age: int, name: str):
        """
        The constructor of the Animal class.
        :param age: represents the age of the animal.
        :param name: represents the name of the animal.
        """
        self._age = age
        self._name = name

    @property
    def name(self):
        """
        This is a property decorator. It is used as a getter to the name member
        since this member is private).
        :return: the name of the animal (to enable printing the data if needed).
        """
        return self._name

    @property
    def age(self):
        """
        This is a property decorator. It is used as a getter to the age member (since this member
        is private).
        :return: the age of the animal (to enable printing the data if needed).
        """
        return self._age

    @abstractmethod
    def speak(self) -> None:
        """
        An abstract method which will be implemented in each inheriting class.
        This function will print to the terminal the way the animal is talking.
        """
        ...

    @classmethod
    def print_details(cls, name, age) -> None:
        """
        This is a method class function. It prints the data of each animal. It gets a class and
        prints the animal's data.
        :param cls: a built in parameter which represents the class.
        :param name: the name of the animal.
        :param age: the age of the animal.
        """
        print("my name is " + str(name) + " and I'm " + str(age))


class Dog(Animal):
    """
    This is the class that represents the dog. It inherits the name and the
    age from it's base class- the Animal class.
    """
    def speak(self) -> None:
        """
        This function prints the sound that the dog does when it speaks.
        """
        print("Bark! Bark!")


class Cat(Animal):
    """
    This is the class that represents the cat. It inherits the name and the
    age from it's base class- the Animal class.
    """
    def speak(self) -> None:
        """
        This function prints the sound that the cat does when it speaks.
        """
        print("Meaaaawo!")


class Sheep(Animal):
    """
    This is the class that represents the sheep. It inherits the name and the
    age from it's base class- the Animal class.
    """
    def speak(self) -> None:
        """
        This function prints the sound that the sheep does when it speaks.
        """
        print("Bheeeee!")


if __name__ == '__main__':
    dog = Dog(13, "Baily")
    dog.speak()
    cat = Cat(5, "Ginger")
    cat.speak()
    sheep = Sheep(3, "Wooly")
    sheep.print_details(sheep.name, sheep.age)
