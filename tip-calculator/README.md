# Tip Calculator 
This Python program calculates the tip amount and final bill amount per person when dining at a restaurant.

## How to Use

Enter the total bill amount when prompted.

Enter the percentage of tip you want to give (10%, 12%, or 15%) when prompted.

Enter the number of people splitting the bill when prompted.

The program will calculate the tip amount, the total bill amount, and the final amount each person should pay.

The final amount will be rounded to 2 decimal places.

The program will display the final amount each person should pay.

## How it Works

The program prompts the user to enter the total bill amount, percentage of tip, and number of people splitting the bill using the input() function.

The float() and int() functions are used to convert the input to the appropriate data type.

The program calculates the total tip amount using the formula total_tip_amount = bill * (tip_percentage / 100).

The program calculates the total bill amount by adding the bill amount to the total tip amount using the formula total_bill_amount = bill + total_tip_amount.

The program calculates the final amount each person should pay by dividing the total bill amount by the number of people splitting the bill using the formula final_amount_per_person = total_bill_amount / number_of_people.

The program rounds the final amount to two decimal places using the round() function.

Finally, the program displays the final amount each person should pay using the print() function.