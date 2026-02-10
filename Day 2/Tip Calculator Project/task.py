print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?\n $"))
tip = int(input("What percentage tip would you like to give?\n 10 12 15\n "))
people = int(input("How many people to split the bill?\n "))

bill_per_person = bill/people
tip = bill_per_person * (tip/100)
bill_with_tip = (bill_per_person + tip)
final_bill = round(bill_with_tip,2)

print(f"Each person should pay: ${final_bill}")