fileObject1 = open("a.txt", 'w')
fileObject1.write("Yaniv")
#re-open the file is wrong w/o Close before
fileObject2 = open("a.txt", 'r')
fileContent = fileObject2.read()
print(fileContent)