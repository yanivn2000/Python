

class Calculator:
    def __init__(self):
        self.sum = 0
    def add(self,x):
        self.sum += x
    def sub(self,x):
        self.sum -= x
    def __str__(self):
        return str(self.sum)


calc1 = Calculator()
print(calc1)
calc1.add(5)
print(calc1)
calc1.add(3)
print(calc1)
calc1.sub(4)
print(calc1)
calc1.sub(1)
print(calc1)

#Output
#5
#8
#4
#3