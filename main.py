
print("Welcome to the Bill Calculator!")

bill = float(input("Enter the total bill: $"))
no_of_people = int(input("How many people sharing the bill? "))
tip_amount = int(input("How much tip you would like to add (10,12,15)? "))



total_bill = round((((tip_amount / 100) * bill ) + bill ) / no_of_people,2)

print(f"Each person has to pay ${total_bill}")