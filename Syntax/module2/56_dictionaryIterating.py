#dictionary to tuples
dict={'k1':'v1', 'k2':'v2', 'k3':'v3'}

#That we know
for k , v in dict.items():
    print(f"{k},{v}")

#iterating to tuples
res = ((k,v) for  k , v in dict.items())

for i in res:
    print(i)

#unpack, formating and insert to list
list = ["%s=%s" % (k,v) for  k , v in dict.items()]

for i in list:
    print(i)