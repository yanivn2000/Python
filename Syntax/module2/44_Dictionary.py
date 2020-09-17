#Dictionary

dic={'k1':'v1', 'k2':'v2', 'k3':'v3'}
print(dic['k2'])

#update
dic['k2']='updated'
print(dic['k2'])

dic['k2']=20
print(dic['k2'])

#add new key-val
dic['k22']=333
print(dic['k22'])

print(dic)

#dictionary of lists
print('dictionary of lists')
dic={'k1':[1,2], 'k2':[3,4], 'k3':[5,6]}
print(dic)
#update
dic['k2'].append(33)
print(dic['k2'])
print(dic)


#Access unexisted key! ERROR
#print(dic['not2'])
