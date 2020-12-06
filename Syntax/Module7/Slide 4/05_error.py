try:
    fileObject1 = open("e.txt", "w")
    fileObject1.write("Yaniv")
    fileObject1.writee("Nuriel") #bug
    print("This is not printed")
    fileObject1.close()
except:
    print("There was an error")

print(fileObject1.closed) #False
#we cannot read it becausefile is still open
fileObject2 = open("e.txt", "r")
fileContent = fileObject2.read()
fileObject2.close()
print(fileContent)