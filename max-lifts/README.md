# 1 REP MAX Calculator 
This Python program calculates the one rep max of a weightlifter based on the weight they lifted and the number of reps they can do with that weight. The program uses the Epley formula to calculate the one rep max.

## How to Use
Run the program using a Python interpreter (e.g. IDLE, PyCharm, or VS Code).

Enter the weight lifted in kilograms when prompted.

Enter the number of reps you can do with that weight when prompted.

The program will then calculate the one rep max using the Epley formula and display the result to the console.

## How it works
The Epley formula is used to calculate the one rep max. The formula is as follows:

**1RM = weight / (1.0278 - 0.0278 x reps)**

Where weight is the weight lifted in kilograms and reps is the number of reps you can do with that weight.

The program begins by prompting the user to enter the weight lifted and the number of reps using the "input" function. The "int" function is used to convert the input to an integer data type.

Next, the program calculates the one rep max using the Epley formula, which is stored in the "maximum" variable. The result is then formatted to two decimal places using the **"{:.2f}"** format specifier.

Finally, the program prints the result to the console using the "print" function.

Overall, the code is a simple and effective way to calculate the one rep max of a weightlifter using the Epley formula.

