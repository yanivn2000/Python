# ***** Parameter #1+2 ***** #

#Accessing string characters in Python
str = 'We use only the finest baby frogs'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

# ***** Parameter #3 ***** #
str='abcdef'
print("\nTesting the string 'abcdef'")
print('str[::-1] = ', str[::-1])
print('str[::2] = ', str[::2])
print('str[1::2] = ', str[1::2])

#do exc_19

# ***** remember that string is mutable! ****** #
#str[0] = 'r' #- ERROR

#We can do the same from list ... later