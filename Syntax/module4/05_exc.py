#Get input from the user
#print how many upper case letter are and how many lower case
#For example
#Please insert a string: Yaniv Nuriel
#Number of upper case caracters: 2
#Number of upper case caracters: 10

def count_letter(str):
    d = {"UPPER_CASE":0, "LOWER_CASE":0}
    for c in str:
        if c.isupper():
            d["UPPER_CASE"] += 1
        else:
            d["LOWER_CASE"] += 1
    print("Number of upper case caracters:", d["UPPER_CASE"] )
    print("Number of upper case caracters:", d["LOWER_CASE"] )

count_letter(input("Please insert a string: "))