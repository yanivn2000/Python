#enforce the user to insert 'hello'
#trim the string
n=input("Please insert 'hello':")
while n.strip() != 'hello':
    n = input("Please insert 'hello':")