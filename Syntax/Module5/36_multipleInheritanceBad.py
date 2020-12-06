#slide 14
#not recommended!

class C:
    def f(self):
        print("C.f")


class D:
    def f(self):
        print("D.f")


class E(C,D):
    pass

e1 = E()
e1.f() # C.f (the first declared..very confusing)
