#also return by reference
def f(d):
    return d #by ref


c = [1,2,3]
e = f(c)
#e--> [1,2,3] <-- c
b = c is e #True
print(b)

