# write doesn't print \n by default
# write returns the number of chars written
with open("output1.txt", 'w') as fileObject:
    fileObject.write("Yaniv\n")
    fileObject.write("Nuriel\n")
    fileObject.write("Bon")
    fileObject.write("John")
