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

c1 = C()
d1 = D()
print(isinstance(c1, C)) #True
print(isinstance(c1, D)) #False
print(isinstance(d1, C)) #True
print(isinstance(d1, D)) #True