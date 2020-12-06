# w+ when file exists it overwrite it
# add 123456789 to the file
fileObject = open("readWrite2.txt", 'w+')

fileContent = fileObject.read()
print(fileContent) # ''
fileObject.write('Yaniv')
fileContent = fileObject.read()
print(fileContent) # ''
