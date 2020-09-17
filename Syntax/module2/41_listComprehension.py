list1 = ['ab', 'cd', 'ef']
list2 = ['k', 'l', 'j']

print(list2)


list3 = []
for string in list1:
    for char in string:
        list3.append((char))

print(list3)