Height = float (input("Enter Your Height Here: "))
Weight = float (input("Enter Your Weight Here: "))
BMI = Weight / (Height/100)**2
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
