#input1 = string
#input2 = string
#output = common letters of s1 and s2
#s1= yaniv
#s2= nuriel
#output:n i


str1 = input("Please insert first string: ")
str2 = input("Please insert second string: ")

s1 = set(str1)
s2 = set(str2)
s3 = s1.intersection(s2)
res = ','.join(s3)
print(res)


