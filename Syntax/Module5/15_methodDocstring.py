#slide 5

class Calculator:
    def add(self,x, y):
        """Add 2 numbers
        :param x: first number
        :param y: second number
        :return: sum of x and y
        """
        return x + y

calc1 = Calculator()
#print(calc1.add(5,7))
print(calc1.add.__doc__)
#Output
#12