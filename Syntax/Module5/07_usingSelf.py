#using self
#1st parameter goes to 2nd parameter...

class C:
    def __init__(self, x, y):
        self.x = x #we save x in data member


c1 = C(5,6)#x = 5 y = 6
print(c1.x)#5
print(c1.y)#AttributeError: 'C' object has no attribute 'y'