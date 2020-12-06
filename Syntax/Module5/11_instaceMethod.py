#slide 5
#instace method (self)
class C:
    def __init__(self, x1):
        self.x = x1

    def f(self):
        print(f"c.f was called, {self.x}")

    def d(self):
        print("c.d was called")

c1 = C(5)
c1.f()

C.f(c1)#like c1.f()
#C.d()#d() missing 1 required positional argument: 'self'