#Python uses the keyword None to define null objects and variables.
# While None does serve some of the same purposes as null in other languages,
# it's another beast entirely. As the null in Python,
# None is not defined to be 0 or any other value.
# In Python, None is an object

b = None
print(b)

print(bool(b))#False

d = b is None
print(d)#True

d = b is not None
print(d)#True