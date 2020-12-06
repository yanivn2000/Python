#slide 14
#not recommended!

class C:
    def f(self):
        print("f")


class D:
    def g(self):
        print("g")


class E(C,D):
    pass

e1 = E()
e1.f() # f
e1.g() # g