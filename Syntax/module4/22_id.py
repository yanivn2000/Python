x=1
a1 = id(x)
print(a1) #4412160704
y = 2
a2 = id(y)
print(a2) #4412160736
z = x
a3 = id(z)
print(a3) #4412160704 (same as x)
b1 = x is z #True
print(b1)

c = 5
a4 = id(c) #4412160832
print(a4)
c += 1
a5 = id(c) #4412160864 - changed
print(a5)

