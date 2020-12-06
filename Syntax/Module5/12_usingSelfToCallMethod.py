#slide 5
#self is the way to call method from method
class C:
    def __init__(self, x):
        self.x = x

    def f(self):
        print("c.f was called")
        self.d()

    def d(self):
        print(f"c.d was called, x:{self.x}")

c1 = C(5)
c2 = C(6)
c1.f()
c2.f()