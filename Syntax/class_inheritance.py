class Mammal:
    def walk(self):
        print("Walk")
    def eat(self):
        print("eat")


class Dog(Mammal):
    #pass (if non implementation)
    def make_sound(self):
        print("bark")
    def eat(self):
        print("dog eat")


class Cat(Mammal):
    #pass
    def make_sound(self):
        print("meow")
    def eat(self):
        print("cat eat")


cat = Cat()
cat.make_sound()
cat.walk()
cat.eat()

dog = Dog()
dog.make_sound()
dog.walk()
dog.eat()