with open('input1.txt', 'r') as fileObject:
    print(fileObject.tell()) # 0
    print(fileObject.read(2)) # Ya
    print(fileObject.tell()) # 2
    print(fileObject.read(4)) # niv
                              #
    print(fileObject.tell()) # 6 (because \n is also s char)

print()
with open('input1.txt', 'rb') as fileObject:
    print(fileObject.tell()) # 0
    print(fileObject.read(2)) # b'Ya'
    print(fileObject.tell()) # 2
    print(fileObject.read(4)) # b'niv\n'
    print(fileObject.tell()) # 6 (because \n is also s char)
