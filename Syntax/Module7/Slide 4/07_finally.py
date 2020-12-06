#using finally instead of with
try:
    try:
        fileObject1 = open("g.txt", "w")
        fileObject1.write("Yaniv")
        fileObject1.writee("Nuriel") #bug
        print("This is not printed")
    finally: #in any case this will be called
        print("This is printed") # printed
        fileObject1.close() #close
except:
    print("There was an error")

print(fileObject1.closed) # True
#we can read it because with the break of with closed the file
fileObject2 = open("e.txt", "r")
fileContent = fileObject2.read()
fileObject2.close()
print(fileContent) # Yaniv