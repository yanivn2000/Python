#Slide 14
#Basic ineritance: members and functions
class C:
    x = 1

    def f1(self):
        print("f1")


class D(C):
    y = 2

    def f2(self):
        print("f2")

d1 = D()
d1.f1() #f1
d1.f2() #f2
print(d1.x)
print(d1.y)