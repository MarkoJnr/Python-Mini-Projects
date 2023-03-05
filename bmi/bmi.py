from termcolor import colored

print("A BMI Calculator will take in the height and weight of the individual and will calculate the BMI of the person.")
print("Body mass index (BMI) is a measure of body fat based on height and weight.")

# Prompt the user for their height and weight
Height = float(input("Enter Your Height Here: "))
Weight = float(input("Enter Your Weight Here: "))

# Calculate the BMI using the formula BMI = Weight / (Height/100)**2
BMI = Weight / (Height/100)**2

# Determine the BMI category using if-elif-else statements and print the category and calculated BMI
if BMI <= 18.4:
    category = "Underweight"
    advice = "You may need to gain weight. Consider consulting with a nutritionist or doctor for advice."
    color = "yellow"
    
elif BMI <= 24.9:
    category = "Healthy"
    advice = "Maintain your healthy weight by continuing to eat a balanced diet and staying active."
    color = "green"
   
elif BMI <= 29.9:
    category = "Overweight"
    advice = "Try to lose weight by eating a balanced diet and exercising regularly. Consider consulting with a nutritionist or doctor for advice."
    color = "magenta"

elif BMI <= 34.9:
    category = "Severely overweight"
    advice = "Losing weight is important for your health. Consider consulting with a nutritionist or doctor for advice."
    color = "red"
    
elif BMI <= 39.9:
    category = "Obese"
    advice = "Losing weight is important for your health. Consider consulting with a nutritionist or doctor for advice."
    color = "red"
    
else:
    category = "Severely obese"
    advice = "Losing weight is important for your health. Consider consulting with a nutritionist or doctor for advice."
    color = "red"

# Print the category and calculated BMI with colored output
print(f"\n Your BMI is {BMI:.1f}. You are {category}.")

# Print the nutritional advice for the BMI category
print(advice)
