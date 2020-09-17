#numbers placeholders
a=1
b="Yaniv"
s1="a is {0}, b is {1}".format(a,b)
print(s1)

#named placeholders
s1="a is {b}, b is {a}".format(a=10,b="Joy")
print(s1)

#Width and aligmnet can be specified
print("{0:<20}Continue".format(("A")))
print("{0:^20}Continue".format(("A")))
print("{0:>20}.".format(("A")))

#Floating point
res=10.0/3
print("{:}".format(res))
print("{:.2f}".format(res))