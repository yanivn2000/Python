#slide #1
#Later on we will implement str overload method
class C:
    pass


c1 = C()
#<__main__.C object at 0x7fabef98fc10>
print(c1)

#<__main__.C object at 0x7fabef9bfdc0>
c2 = C()
#<class '__main__.C'>
print(c2)

#<__main__.C object at 0x7fabef9bfdc0>
c3 = c2
#<class '__main__.C'>
print(c3)