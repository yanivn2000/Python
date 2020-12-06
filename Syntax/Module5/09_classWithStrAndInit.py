#str + init
class C:
    def __init__(self, x):
        self.x = x


    def __str__(self):
        return f"x = {self.x}"



c1 = C(5)

print(c1)#This is C
