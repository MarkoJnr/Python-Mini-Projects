## Leap Year Checker
This Python script checks whether a given year is a leap year or not. It also provides brief explanation of why leap years exist and how they are calculated. This information is printed to the console after the leap year check is performed.

## How to use

When prompted, enter a year that you would like to check (e.g. 2000).

The script will output a message indicating whether the year is a leap year or not.

If the year is a leap year, the script will also output the fact that leap years have an extra day (February 29) to keep the calendar year synchronized with the astronomical year.

If the year is not a leap year, the script will also output the fact that a year is not a leap year if it is divisible by 100 but not divisible by 400.

## How it works

The script uses the **modulo operator** (%) to determine whether the input year is evenly divisible by 4, 100, and 400. 

If the year is divisible by 4 but not by 100, it is a leap year. 

If the year is divisible by 100 but not by 400, it is not a leap year. 

If the year is divisible by both 100 and 400, it is a leap year.
