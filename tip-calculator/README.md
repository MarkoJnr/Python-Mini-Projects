# Tip Calculator 
This Python program calculates the tip amount and the final bill amount per person when dining at a restaurant. The program prompts the user to enter the total bill, the percentage of tip they want to give, and the number of people splitting the bill.

## How to Use
Run the program using a Python interpreter (e.g. IDLE, PyCharm, or VS Code).
Enter the total bill amount when prompted.
Enter the percentage of tip you want to give (10%, 12%, or 15%) when prompted.
Enter the number of people splitting the bill when prompted.
The program will calculate the tip amount, the total bill amount, and the final amount each person should pay.
The final amount will be rounded to 2 decimal places.

## Formula Used
The formula used to calculate the total tip amount is:

total_tip_amount = bill * (tip_percentage / 100)

Where bill is the total amount of the bill and tip_percentage is the percentage of tip that the user wants to give.

The formula used to calculate the total bill amount is:

total_bill_amount = bill + total_tip_amount

Where bill is the total amount of the bill and total_tip_amount is the amount of tip calculated in the previous step.

The formula used to calculate the final amount each person should pay is:

final_amount_per_person = total_bill_amount / number_of_people

Where total_bill_amount is the total bill amount calculated in the previous step and number_of_people is the number of people splitting the bill entered by the user.

## Code Explanation
The program begins by prompting the user to enter the total bill amount, percentage of tip, and number of people splitting the bill using the "input" function. The "float" and "int" functions are used to convert the input to the appropriate data type.

Next, the program calculates the total tip amount using the formula above and stores it in the "total_tip_amount" variable.

Then, the program calculates the total bill amount by adding the bill amount to the total tip amount and stores it in the "total_bill_amount" variable.

Next, the program calculates the final amount each person should pay by dividing the total bill amount by the number of people splitting the bill and rounds it to two decimal places using the "round" function.

Finally, the program displays the final amount each person should pay using the "print" function.
