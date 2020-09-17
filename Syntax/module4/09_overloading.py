def ab():
    print("a")

ab() #a

def ab():
    print("b")

ab() #b

def ab(a,b):
    print(a,b)

#ab()#TypeError: ab() missing 2 required positional arguments: 'a' and 'b'
ab(1,3)