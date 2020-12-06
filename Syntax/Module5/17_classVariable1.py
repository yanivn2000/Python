#Class variable
class C:
    myClassVariable = 1

    def __init__(self,x):
        self._x = x

    def get_x(self):
        return self._x


c1 = C(2)
c2 = C(3)
print(c1.get_x()) # 2
print(c2.get_x()) # 3
print(C.myClassVariable) # 1
print(c1.myClassVariable) # 1 (through instance)
#C.get_x() #missing 1 required positional argument: 'self'