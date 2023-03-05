# Prompt the user for information
print ("Welcome to the tip calulcator.\n")
bill = float(input("What was the total bill? £"))
tip = int(input("What Percentage tip would you like to give? 10,12 or 15?\n"))
people = int(input("How many people to split the bill?\n"))

# Calculate tip and total bill amount
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount

# Calculate the final amount per person and round to two decimal places
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

# Print the final amount owed by each person
print(f"Each person should pay: £{final_amount}")
