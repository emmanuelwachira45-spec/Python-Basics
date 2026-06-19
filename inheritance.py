#Parent Class/ Super Class / Base Class
class Animal:

    isMammal = True

    def sound(self):
        print("Animal is making a sound")

class Cat(Animal):
    hasFur = True
    def sleep(self):
        print("Cat is sleeping")

class Cow(Cat):
    has_Horns = True


mycow = Cow()


mycat = Cat()
