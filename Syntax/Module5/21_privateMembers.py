#strongely private conversion __x
class C:
    myClassVariable = 1

    def __init__(self,x):
        self.__x = x
    def get_x(self):
        return self.__x


c1 = C(2)
print(c1.get_x()) # 2
print("Start..")
#warning, but it continues:
# can access but it is against the conversion agreed
print(c1.__x) # 2 - can access but it is against the conversion agreed

print("End..")