# ***** is functions ****** #
s1="a b"
s2="12"
s3="CD"
s5="CD123"
s4=" "

s1.isalpha()#False
s2.isalpha()#False
s3.isalpha()#True
s4.isalpha()#False

s1.isalnum()#False
s2.isalnum()#True
s3.isalnum()#True
s4.isalnum()#False

s1.isdigit()#False
print(s2.isdecimal())#True
s3.isdigit()#False
s4.isdigit()#False

s1.isspace()#False
s2.isalpha()#False
s3.isalpha()#False
s4.isalpha()#True