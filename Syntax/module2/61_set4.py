#set discard
s = {1,2,3}
s.discard(1)
print(s)
s.discard(4)#no exception although 4 is missing
print(s)

#.remove will give indication of failure