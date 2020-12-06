#closed - bool
fileObject1 = open("a.txt", 'w')
print(fileObject1.closed)
fileObject1.close()
print(fileObject1.closed)
