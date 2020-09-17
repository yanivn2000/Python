l = [1,2,3]
s = l
# l --> [1,5,3] <-- s
s[1] = 5
print(l[1]) #5
print(l is s) #True
print(l)
print(s)

a = [1,2]
b = [1,2]
#a --> [1,2]
#b --> [1,2]
print(a == b) #True
print(a is b) #False