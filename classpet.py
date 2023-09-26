
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self, n):
        for _ in range(n):
            print("bark!")

    def human_age(self):
        return self.age * 4

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self, n):
        for _ in range(n):
            print("meow~")

    def human_age(self):
        return self.age * 4


bark_count = int(input("짖을 횟수: "))
dog_name = input("Name: ")
dog_age = int(input("Age: "))
my_dog = Dog(dog_name, dog_age)
my_dog.bark(bark_count)
print(my_dog)
print("사람 나이로 환산:", my_dog.human_age())


meow_count = int(input("울을 횟수: "))
cat_name = input("Name: ")
cat_age = int(input("Age: "))
my_cat = Cat(cat_name, cat_age)
my_cat.meow(meow_count)
print(my_cat)
print("사람 나이로 환산:", my_cat.human_age())
