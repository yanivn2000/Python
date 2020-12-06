#slide 11
#GC reference counter

class C:
    def __init__(self):
        print("__init__ is called")

    def __del__(self):
        print("__del__ is called")

c1 = C()
#c1--> $
c2 = c1
#c1 --> $ <-- c2
print("Yaniv")
c1 = None
#c1 --> None
# $ <-- c2
#c2 still has reference to the memory
#this is way GC doesn't release it
while True:
    pass
#__init__ is called
#Yaniv
