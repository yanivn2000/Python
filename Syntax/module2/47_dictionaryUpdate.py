#update dictionary using another dictionary

dic={'k1':'v1', 'k2':'v2', 'k3':'v3'}
dic2={'k33':'v33', 'k1':'v44'}
print(dic)

#k33 will
dic.update(dic2)
print(dic)

print()
dic2={'k1':'v11'}
dic.update(dic2)
print(dic)