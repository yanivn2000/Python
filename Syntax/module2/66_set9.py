#method returns True if a set has every elements of another set
s1 = {1,3,4}
s2 = {4,5,6}
s3 = {4,3,2,1,0}

#is s3 is a superset of s1
print(s3.issuperset(s1)) #True
#is s2 is a superset of s1
print(s2.issuperset(s1))#False

#subset (opposit to above)
print(s1.issubset(s3)) #True
