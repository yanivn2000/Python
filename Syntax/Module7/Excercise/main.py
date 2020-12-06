from my_file import MyFile

with open('a.txt', 'w') as fileObject:
    fileObject.write('Amir Adler')

myFile = MyFile('a.txt') # Am
print(myFile.read(2)) # ir
print(myFile.read(2)) # Amir A
myFile.reset()
print(myFile.read(6))
print(myFile.get_name()) # a.txt
print(myFile.get_mode()) # r
print(myFile.is_closed()) # False
myFile.close()
print(myFile.is_closed()) # True
