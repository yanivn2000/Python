#slide 4
class Person:

    def __init__(self, name):
        self.name = name
        persons.append(self)


    def __str__(self):
        return self.name


persons = []
p1 = Person("Yaniv")
p2 = Person("Nuriel")

for p in persons:
    print(p)
#Yaniv
#Nuriel


