#slide 10
# #Class variable
class C:
    myClassVariable = 1

    def __init__(self,x):
        self._x = x
    def get_x(self):
        return self._x


c1 = C(2)
print(c1.get_x()) # 2
#see warning using mouse over: Access to a protected member _x of a class
print(c1._x) # 2 - can access but it is against the conversion agreed
