class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed


def bark(self):
    print("Dog is barking")

dog1 = Dog("Bob", 4, "Chihuahua")
print(dog1.name, dog1.age, dog1.breed)
dog1.bark()



dog2 = Dog("Brenda", 5, "Husky")