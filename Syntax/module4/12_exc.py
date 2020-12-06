#Write a function that gets 2 parameters:
#1. Word
#2. char for border (optional)
#The char will be printed as the number of chars in the word, before and after it
#In case the input is: Yaniv and no char is given then the output is:
#-----
#Yaniv
#-----
#In case the char like * is given we print the char instead of the -
#***
#Hey
#***

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("Yaniv")
banner("Hey","*")