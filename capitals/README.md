## Capital City Quiz Game

This is a Python script that tests your knowledge of capital cities of different countries. It starts with a set of 10 easy questions, and if the user answers correctly for at least 8 of them, the script generates a set of 10 random questions with increasing difficulty.

## How to use

Clone or download the repository to your local machine.

Navigate to the directory containing the script.

Run the script using the command **python capitals.py**

Answer each question by typing the name of the capital city and pressing Enter.

After completing the quiz, the script will display your score and give you the option to take the advanced quiz if you passed.

## How it works

The script uses a dictionary to store the names of different countries as keys and their corresponding capital cities as values. 

It then uses a loop to iterate over each item in the dictionary and ask the user to enter the capital city name for each country. 

The user's input is compared to the correct answer for each question, and a score is calculated based on the number of correct answers.

If the user scores at least 8 out of 10 on the easy quiz, the script generates a new set of 10 questions using the **random.sample** method. 

If the user's score is less than 8, the program ends with a message encouraging the user to work on their capital city knowledge.

The user who passed is asked to enter the capital city name for each country, and a new score is calculated based on the number of correct answers.

At the end of the quiz, the user's score and the number of questions asked are displayed, along with a message indicating whether they passed the quiz or not. 