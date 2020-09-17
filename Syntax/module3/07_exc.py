#Print the numbers between 1-40
#The program will not print the numbers that are multiply of 5 or 7


for num in range(1,40,2):
    if(num % 5 and num % 7 ):
        print(num)