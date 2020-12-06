#slide 11
#if I don't need to this is a good solution to tell GC that we don't need this resources anymore

class C:
    def __init__(self):
        print("__init__ is called")

    def __del__(self):
        print("__del__ is called")

c1 = C()
print("Yaniv")
c1 = None
while True:
    pass
#__init__ is called
#Yaniv
#__del__ is called
