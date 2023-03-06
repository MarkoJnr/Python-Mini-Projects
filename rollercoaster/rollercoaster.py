# Welcome message
print("Welcome to the Python Rollercoaster!")

# Get user's height in centimeters
height = int(input("What is your height in cm?: "))

# Set initial ticket price to 0
bill = 0

# Check if user is tall enough to ride the rollercoaster
if height >=120:
    # If the user is tall enough, ask for their age to determine the price of their ticket
    print ("You can ride the rollercoaster!")
    age = int (input("How old are you?: "))
    
    # Determine the ticket price based on the user's age
    if age <=12:
        print ("1 Child ticket is £3")
        bill +=3
    elif age <=18:
        print ("1 Youth ticket is £5")
        bill +=5
    else:
        print ("1 Adult ticket is £7")
        bill +=7
    
    # Ask if the user wants a photo and update the ticket price accordingly
    wants_photo = str(input("Would you like a photo? Yes or No: "))
    yes_photo = bill +3
    if wants_photo == "Yes":
        print (f"Your final ticket price will be £{yes_photo}. Enjoy the Ride!")
    else: 
        print (f"Your final ticket price will be £{bill}. Enjoy the Ride!")
else:
    # If the user is not tall enough, print a message informing them that they cannot ride
    print ("Sorry you are not tall enough to ride the rollercoaster.")
