with open("input1.txt", 'r') as fileContent:
    print(fileContent.read(2)) # Ya
    print(fileContent.read(1)) # n
    print(fileContent.read(4)) # iv
                               # N
    print(fileContent.read(10)) #uriel
    print(fileContent.read(1)) # ''

print('end')