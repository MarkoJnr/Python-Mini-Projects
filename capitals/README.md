## Capital City Quiz Game

This is a Python script that tests your knowledge of capital cities of different countries. It starts with a set of 10 easy questions, and if the user answers correctly for at least 8 of them, the script generates a set of 10 random questions with increasing difficulty.

## How to use

When you run the game, you will be asked to provide the capital of each country.

Type your answer and press "Enter". If your answer is correct, you will receive a message saying "Correct!" and your score will increase by 1. 

If your answer is incorrect, you will receive a message saying "Incorrect. The capital of [country] is [capital]." and your score will remain the same.


## How it works

The game is divided into two parts. The first part consists of 10 predetermined questions, where you will be asked to provide the capital of a given country.

The second part consists of 10 randomly selected questions from a list of 195 countries and their capitals.

The script uses a dictionary to store the names of different countries as keys and their corresponding capital cities as values. 

It then uses a loop to iterate over each item in the dictionary and ask the user to enter the capital city name for each country. 

The user's input is compared to the correct answer for each question, and a score is calculated based on the number of correct answers.

If the user scores at least 8 out of 10 on the easy quiz, the script generates a new set of 10 questions using the **random.sample** method. 

If the user's score is less than 8, the program ends with a message encouraging the user to work on their capital city knowledge.

At the end of the game, you will receive a message telling you your final score out of the total number of questions.