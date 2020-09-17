#remove the common elements
s1 = {1,3,4}
s2 = {4,5,6}

#returns set without the duplication
print(s1.symmetric_difference(s2))#1,3,5,6
#unchanged
print(s1,s2)