#Slide 14
#call parent

class C (A):
    def __init__(self,x):
        self._x = x

    def get_x(self):
        return self._x


class D(C):
    def __init__(self,x,y):
        #call parent constructor
        super().__init__(x)
        self._y = y

    def get_y(self):
        return self._y


d1 = D(1,2)
print(d1.get_x()) # 1
print(d1.get_y()) # 2