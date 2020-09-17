a = True
print(a)#True

b = False
print(b)#False

#Casting
print(int(a))#1
print(int(b))#0
print(str(a))#True
print(str(b))#False
print(bool(0))#False
print(bool(4))#True
print(f"bool(-4) {bool(-4)}")#True
print(bool(""))#False
print(bool("cool"))#True
print(bool("True"))#True
print(bool("False"))#True

print("*** None testing ***")
k=None
print(k) #None
print(bool(k))#bool(None) -- > False
#print(int(k)) #ERROR!
print(str(k))

