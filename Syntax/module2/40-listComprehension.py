#dup every element
list = range(1,11)
for i in list:
    print(i)

list = [i*2 for i in list]
print(list)

list2 = []
for i in list:
    list2.append((i*2))

print(list2)