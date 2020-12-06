#slide 5
#this is the convesion to wrap the
# get and set of the data members (C++)
class C:
    def __init__(self,x):
        self.x = x
    def get_x(self):
        return self.x
    def set_x(self, x):
        self.x = x

c1 = C(5)
print(c1.get_x()) # 5

c1.set_x(6)
print(c1.get_x()) # 6
