str="this OK a string example"
s1=str.startswith("this")#True
s2=str.startswith("is",2,4)#True
s3=str.startswith("this",2,4)#False

print(s1,s2,s3)