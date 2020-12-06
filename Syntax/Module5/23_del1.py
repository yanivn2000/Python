#slide 11
#external resources are to be managed by the program
#GC reference counter
#Example shows that python releases its managed resources


class C:
    def __init__(self):
        print("__init__ is called")

    def __del__(self):
        print("__del__ is called")

c1 = C()
print("Yaniv")
#__init__ is called
#Yaniv
#__del__ is called