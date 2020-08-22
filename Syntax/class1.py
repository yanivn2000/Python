class Person:
    def __init__(self,name):
        self.name = name
        
    def info(self):
        print(f"My name is {self.name}")


person1 = Person("Yaniv Nuriel")
person1.address = "Lea 14, Tel Aviv"
person1.info()
print(f"{person1.address}")
person2 = Person("Danny Boy")
person2.info()