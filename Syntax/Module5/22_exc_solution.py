class Person:
    id = 1

    def __init__(self, name):
        self.__id = Person.id
        Person.id += 1
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        return f"id: {self.__id}, name: {self._name}"

p1 = Person("Yaniv")
print(p1.get_name())
print(p1)
p2 = Person("Bob")
print(p2.get_name())
print(p2)
