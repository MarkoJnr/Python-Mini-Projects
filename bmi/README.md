# Body Mass Index (BMI) Calculator 
This is a simple program that calculates your BMI based on your height and weight, and tells you whether you are underweight, healthy, overweight, severely overweight, obese, or severely obese.

## How to use
Enter your height in centimeters when prompted.

Enter your weight in kilograms when prompted.

The program will calculate your BMI and display your weight category.

## How it works
The program prompts the user to enter their height and weight.

The user's input is stored as floats in the Height and Weight variables.

The program calculates the BMI by dividing the user's weight in kilograms by the square of their height in meters. The formula is:

BMI = Weight / (Height/100)**2

The program uses if-elif statements to check which weight category the user falls into based on their BMI.

The program prints a message telling the user which weight category they fall into.