# first writen 123456789 to the file readWrite1.txt
# r+ read and open, but the file must exist
# The file points to the begining of the file
fileObject = open("readWrite1.txt", 'r+')

fileObject.write('Yaniv')
fileContent = fileObject.read() #change the pointer after Yaniv
print(fileContent) # 6789
fileObject.write('Nuriel')
fileContent = fileObject.read() # change the pointer after Yaniv that is end of file
print(fileContent) # ''