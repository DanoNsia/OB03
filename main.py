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
    print(animals.make_sound())

dog = Animal
popka = Bird
tortoises = Turtle

animal_sound(dog)
animal_sound(popka)
animal_sound(tortoises)