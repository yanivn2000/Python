has_good_records = True
has_learning_completed = False
avg_scores = 95
num_of_scores = 12

degree_type = input("Degree type (B) for BA and (M) for MBA): ")
if degree_type.upper() == "B":
    print("Your degree is in BA")
elif degree_type.upper() == "M":
    print("Your degree is in MBA")
else:
    print("Unknown degree")

#and/or/not
if has_good_records and not has_learning_completed:
    print("Eligible for degree")
elif has_learning_completed:
    print("Not eligible for degree")

if avg_scores > 90:
    print("Outstanding score!")

