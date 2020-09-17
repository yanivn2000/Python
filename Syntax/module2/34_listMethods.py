#list methods

#append
list=[1,2,3,4]
list.append(5)
print(list)

#popo the last value
list.pop()
print(list)

#insert in position 2 the value 88
list.insert(2,88)
print(list)

#remove object 88
list.remove(88)
print(list)

del list[2]
print(list)

#extend (end)
list+=[99,100]
print(list)
list.extend([101,102])
print(list)

#remove
list.remove([-101,-102])
print(list)
