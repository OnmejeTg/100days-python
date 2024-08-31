print("Welcome to the tip calculator!")

total_bill = float(input("Enter the total bill amount: "))
tip_percent = float(input("How much tip  would you like to give? 10, 12, or 15?"))
number_of_people = float(input("How many people to split the bill?"))

tip_amount = total_bill * (tip_percent / 100)

final_amount = total_bill + tip_amount

final_amount_per_person = final_amount / number_of_people

print(f"The final amount per person is ${final_amount_per_person:.2f}")
