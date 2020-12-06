#str
class B:
    pass


class C:
    def __str__(self):
        return ("This is C")


b1 = B()
print(b1)#<__main__.B object at 0x7f92a288fc10>
c1 = C()
print(c1)#This is C
