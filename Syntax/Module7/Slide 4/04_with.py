
with open("d.txt", 'w') as fileObject1:
    print(fileObject1.closed) # False
    fileObject1.write("Yaniv")
#after with block the file is closed
print(fileObject1.closed) #True
with open("d.txt", 'r') as fileObject2:
    fileContent = fileObject2.read()
    print(fileContent)