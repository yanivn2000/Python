#list that can not be modified
#like a list (operators)

a = (1,2,3)
(a,b,c) = a
print(a,b,c)
#e,f,g = a


a = [1,2,3]
b = tuple(a) #1,2,3
print(b)
c = "Hey"
d = tuple(c) #'H', 'e', 'y'
print(d)

#extra
h="Yaniv"
i="Nuriel"
h,i = i, h
print(h,i)