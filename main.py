#1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`)
# и методы (`make_sound()`, `eat()`) для всех животных.

#2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).

#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.

#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

#5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`,
# которые могут иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

#Дополнительно:
#Попробуйте добавить дополнительные функции в вашу программу,
# такие как сохранение информации о зоопарке в файл и возможность её загрузки,
# чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.


class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"{self.name} издаёт звук")

    def eat(self):
        print(f"{self.name} кушает")

cat = Animal("borsch","12")
cat.make_sound()
cat.eat()

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} поёт")

    def fly(self):
        print(f"{self.name} летает")

bird = Bird("aloha","2")
bird.make_sound()
bird.eat()
bird.fly()

class Turtle(Animal):
    def make_sound(self):
        print(f"{self.name} шипит")

    def how_old(self):
        print(f"{self.name} живёт всего {self.age} лет")

turtle = Turtle("monya","257")
turtle.make_sound()
turtle.eat()
turtle.how_old()

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Животное {animal.name} добавлено в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Сотрудник {staff_member.name} добавлен в зоопарк.")

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

# Создание списка животных и демонстрация полиморфизма
animals = [cat, bird, turtle]
animal_sound(animals)

# Создание зоопарка и добавление животных и сотрудников
zoo = Zoo()
zoo.add_animal(cat)
zoo.add_animal(bird)
zoo.add_animal(turtle)

# Создание сотрудников и добавление их в зоопарк
zookeeper = ZooKeeper("Alice")
veterinarian = Veterinarian("Bob")
zoo.add_staff(zookeeper)
zoo.add_staff(veterinarian)

# Использование методов сотрудников
zookeeper.feed_animal(cat)
veterinarian.heal_animal(bird)