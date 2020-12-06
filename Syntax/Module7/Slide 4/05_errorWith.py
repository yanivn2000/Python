try:
    with open("f.txt", "w") as fileObject1:
        fileObject1.write("Yaniv")
        fileObject1.writee("Nuriel") #bug
        print("This is not printed")
        #no need to explicitly clsoe it
except:
    print("There was an error")

print(fileObject1.closed) # True
#we can read it because with the break of with closed the file
fileObject2 = open("e.txt", "r")
fileContent = fileObject2.read()
fileObject2.close()
print(fileContent)