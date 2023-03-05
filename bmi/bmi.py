# Print a message explaining what a BMI calculator does
print ("A BMI Calculator will take in the height and weight of the individual and will calculate the BMI of the person. \nBody mass index (BMI) is a measure of body fat based on height and weight. ")

# Prompt the user for their height and weight
Height = float (input("Enter Your Height Here: "))
Weight = float (input("Enter Your Weight Here: "))

# Calculate the BMI using the formula BMI = Weight / (Height/100)**2
BMI = Weight / (Height/100)**2

# Determine the BMI category using if-elif-else statements and print the category and calculated BMI
if BMI <= 18.4:
    print(f" Your BMI is {BMI}. You are underweight.")
elif BMI <= 24.9:
    print(f" Your BMI is {BMI}. You are healthy.")
elif BMI <= 29.9:
    print(f" Your BMI is {BMI}. You are overweight.")
elif BMI <= 34.9:
    print(f" Your BMI is {BMI}. You are severely over weight.")
elif BMI <= 39.9:
    print(f" Your BMI is {BMI}. You are obese.")
else:
    print(f" Your BMI is {BMI}. You are severely obese.")
