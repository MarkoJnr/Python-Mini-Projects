import random

# Prompt the user to input names separated by commas
random_names = input("Type your names followed by a comma:")

# Split the input string into a list of names
names = random_names.split(",")

# Get the total number of names
num_items = len(names)

# Generate a random index within the range of the list
random_choice = random.randint(0, num_items - 1)

# Select a person from the list based on the random index
person_who_will_pay = names[random_choice]

# Print the chosen person's name with a message
print(person_who_will_pay + " will pay for this bill.")
