fileObject1 = open("a.txt", 'w')
fileObject1.write("Yaniv")

fileObject1.close() #fixes

fileObject2 = open("a.txt", 'r')
fileContent = fileObject2.read()
print(fileContent)