## Bill Roulette

This is a simple Python script that randomly selects a person from a given list of names to determine who will pay for a bill.

## How to Use

Run the script by executing the following command: Python bill_roulette.py

You will be prompted to type in the names of the participants, separated by commas.
.
The script will randomly select a person from the provided names and display their name as the one who will pay for the bill.

## How It Works

The script begins by importing the **random** module, which allows for generating random numbers.

It prompts the user to enter the names of the participants, separated by commas.

The input string is split into a list of names using the **split(",")** method.

The total number of names is determined using the **len()** function and stored in the num_items variable.

A random index is generated using **random.randint**(0, num_items - 1), which selects a random number between 0 and num_items - 1.

The person who will pay for the bill is selected from the list of names using the randomly generated index.

The chosen person's name is displayed along with the message "will pay for this bill."