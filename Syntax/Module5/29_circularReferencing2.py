#slide 13 - Context managment
#The solution - Context Manager (like using in C#)
#Memory is managed by scope
#With - doesn't need the reference counter to handle the memory

class C:
    def __init__(self):
        print("__init__ is called")
    #init resources allocation
    #this is NOT the __init__
    def __enter__(self):
        print("__enter__ is called")
        return self
    #release resources
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__ is called")

    def __del__(self):
        print("__del__ is called")

c3 = C()
c3 = None;

#with calls __enter__
print("start")
with C() as c1:
    print(c1)
print("end")

#end of scope calls __exit__


#__enter__ is called
#<__main__.C object at 0x7fc88c790c10>
#__exit__ is called