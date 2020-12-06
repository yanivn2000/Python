with open('input1.txt', 'rb') as fileObject:
    print(fileObject.read(2)) # b'Ya'
    fileObject.seek(0) # default is from beginning
    print(fileObject.read(2)) # b'Ya'
    fileObject.seek(1, 0) # from beginning
    print(fileObject.read(2)) # b'an'
    fileObject.seek(-2, 1) #from current position
    print(fileObject.read(2)) # b'an'
    fileObject.seek(-3, 2) # from the end of file
    print(fileObject.read(2)) # b'ie'
