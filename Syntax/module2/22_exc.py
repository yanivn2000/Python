#read a string
#do not change the first 2 characters
#uppercase the 3-4 characters and the rest to lower case
#For example:
#AbCdEf ===> AbCDef

s=input("Please enter a string:")
res=s[:2] + s[2:4].upper() + s[4:].lower()
print(res)