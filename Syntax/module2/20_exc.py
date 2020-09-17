#Replace the first with the last characters
#all the other characters stay the same.


s=input("Please enter a string:")
res=s[-1:] + s[1:-1] + s[:1]
#res=s[-1] + s[1:-1] + s[0]

print(res)