class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("Some generic sound")

    def eat(self):
        print(f"{self.name} is eating.")

class Bird(Animal):
    def make_sound(self):
        print("Chirp chirp!")

class Mammal(Animal):
    def make_sound(self):
        print("Roar!")

class Reptile(Animal):
    def make_sound(self):
        print("Hiss!")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        if isinstance(animal, Animal):
            self.animals.append(animal)
            print(f"{animal.name} has been added to the zoo.")
        else:
            print("This is not an animal!")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} has been added to the zoo staff.")

class ZooStaff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(ZooStaff):
    def feed_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} is feeding {animal.name}.")

class Veterinarian(ZooStaff):
    def heal_animal(self, animal):
        if isinstance(animal, Animal):
            print(f"{self.name} is treating {animal.name}.")


# Пример использования
zoo = Zoo()
bird = Bird("Tweety", 2)
lion = Mammal("Simba", 4)
snake = Reptile("Viper", 5)

zoo.add_animal(bird)
zoo.add_animal(lion)
zoo.add_animal(snake)

zookeeper = ZooKeeper("Bob")
veterinarian = Veterinarian("Alice")

zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

animal_sound([bird, lion, snake])  # Демонстрация полиморфизма

zookeeper.feed_animal(bird)  # Демонстрация работы сотрудников зоопарка
veterinarian.heal_animal(snake)