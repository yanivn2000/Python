#slide 11
#GC reference counter

class C:
    def __init__(self):
        print("__init__ is called")

    def __del__(self):
        print("__del__ is called")

c1 = C()
c2 = c1
print("Yaniv")
c1 = None
c2 = None
#0 references
while True:
    pass
#__init__ is called
#Yaniv
#__del__ is called
