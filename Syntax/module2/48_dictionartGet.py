#get method (to avoid error when key is missing)
dic={'k1':'v1', 'k2':'v2', 'k3':'v3'}
#print(dic[["knot"]])
elm=dic.get('k1', 100)
print(elm)
elm=dic.get('kNOT', 100)
print(elm)
elm=dic.get('kNOT')
print(elm)
