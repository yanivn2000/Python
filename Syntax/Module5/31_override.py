#Slide 14
#Basic ineritance: members and functions
#simply named the same function/memebr name

class C:
    x = 1
    y = 3
    def f1(self):
        print("C.f1")


class D(C):
    x = 2 #member override

    def f1(self): #method override
        print("D.f1")

    def __str__(self):
        return "Yaniv"


d1 = D()
d1.f1() #D.f1
print(d1.x) #2
