print ("Leap Year Checker! Find out if you was born on a leap year!")
year = int(input("Pick a year!:\n"))
if year %4 ==0:
 print (f"{year} is a leap year! ")
elif year %100 ==0:
 print (f"{year} is not a leap year!")
elif year %400 ==0:
 print (f"{year} is a leap year!")
else:
 print (f"{year} is not a leap year")
print ("If a year is divisible by 4, it is a leap year. This is because leap years have an extra day (February 29) to keep the calendar year synchronized with the astronomical year. If a year is divisible by 100, it is not a leap year, unless it is also divisible by 400. This is because a year is not a leap year if it is divisible by 100 but not divisible by 400.")