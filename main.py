class Animal:
    def __init__(self, name, age,scale):
        self.name = name
        self.age = age
        self.scale = scale

    def make_sound(self):
        raise NotImplementedError("использовать в подклассах")

    def eat(self):
        print(f"{self.name} кушает")


class Bird(Animal):
    def __init__(self, name, age, scale):
        super().__init__(name, age, scale)


    def make_sound(self):
        print(f"{self.name} ругается матом.")


class Mammal(Animal):
    def __init__(self, name, age, scale):
        super().__init__(name, age, scale)


    def make_sound(self):
        print(f"{self.name} рычит.")


class Reptile(Animal):
    def __init__(self, name, age, scale):
        super().__init__(name, age, scale)


    def make_sound(self):
        print(f"{self.name} шипит.")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Employee:
    def __init__(self, name):
        self.name = name


class ZooKeeper(Employee):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")


class Veterinarian(Employee):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} принят в зоопарк")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Сотрудник {employee.name} принят на работу.")

    def show_animals(self):
        print("Список животных:")
        for animal in self.animals:
            print(f'название животного :{animal.name},возраст:{animal.age},окрас:{animal.scale}')


    def show_employees(self):
        print("Список сотрудников:")
        for employee in self.employees:
            print(employee.name)


parrot = Bird(name="попугай", age=2, scale="желтый")
lion = Mammal(name="лев", age=5, scale="оранжевый")
snake = Reptile(name="змiй", age=3, scale="коричневая чешуя")


zookeeper = ZooKeeper(name="Ваня")
vet = Veterinarian(name="Доктор Марк Александрович")

zoo = Zoo()
zoo.add_animal(parrot)
zoo.add_animal(lion)
zoo.add_animal(snake)
zoo.add_employee(zookeeper)
zoo.add_employee(vet)
animal_sound(zoo.animals)
zoo.show_animals()
zoo.show_employees()
zookeeper.feed_animal(lion)
vet.heal_animal(snake)