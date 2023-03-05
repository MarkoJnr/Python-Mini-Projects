# Print a message explaining what a one-rep max is
print ("Calculate your one-rep max (1RM) for any lift. Your one-rep max is the max weight you can lift for a single repetition for a given exercise.")

# Prompt the user for information
weight = int (input("Pick a weight lifted in KG:\n"))
reps = int (input ("How many reps can you do with this weight?:\n"))

# Calculate the one-rep max using the Epley formula
maximum = weight / ( 1.0278 - 0.0278 * reps )

# Format the one-rep max to two decimal places
maximum ="{:.2f}".format (maximum)

# Print the one-rep max
print (f"Your 1 one rep max is {maximum}")
