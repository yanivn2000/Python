list = ['a','b','c','d','e']

for elm in list:
    print(elm)#a,b,c,d,e

print(len(list)) #5

for i in range(5):
    print(i) #1,2,3,4,5

for i in range(len(list)):
    print(i) #1,2,3,4,5

for i in range(len(list)):
    print(list[i])#a,b,c,d,e
