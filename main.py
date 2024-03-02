# Importing the os module to interact with the operating system
import os  
# Importing the custom art module for displaying ASCII art
import art  
# Importing warnings module to suppress any warnings
import warnings  
# Ignoring warnings
warnings.filterwarnings("ignore")  


# Initialize 'again' variable to True to start the bidding process
again = True  
while again:

    # Create an empty dictionary to store bidder names and their bids
    store = {}  
    # Initialize the bidding process for a new item
    bidding = True  
    # Prompt user to enter the item being bid on
    peice = input("What are you Bidding on?:\n")  
    # Clear the screen
    os.system('cls')  


    while bidding:
        print(art.logo)
        print(f"Welcome to the secret auction program for {peice}.")  # Display welcome message
        name = input("What is your name?:\n")  # Prompt user to enter their name
        bid = int(input("What's your bid?:\n$"))  # Prompt user to enter their bid
        
        # Function to store bidder's name and bid in the 'store' dictionary
        def bids(name, bid):
            store[name] = bid
        
        # Call the bids function to store bidder's name and bid
        bids(name, bid)
        # Ask if there are any other bidders
        again = input("Are there any other bidders? Type 'yes' or 'no'.").lower()

        if again == "yes":
            os.system('cls')  # Clear the screen for a new bidder

        else:
            bidding = False  # End the bidding process for the current item
            os.system('cls')  # Clear the screen

    final = {}  # Initialize dictionaries to store the final winner(s) and draws
    draw = {}

    for items in store:
        if final == {}:
            final[items] = store[items]  # Assign the first bidder as the potential winner

        else:
            for list in final:

                if store[items] > final[list]:
                    final = {}  # Reset the 'final' dictionary if a higher bid is found
                    draw = {}
                    final[items] = store[items]  # Update the potential winner

                elif store[items] == final[list]:
                    draw[items] = store[items]  # Add the bidder to the draw dictionary
                    draw[list] = final[list]

    print(art.logo) 
    if draw == {}:
        for list in final:
            print(f"The winner of bid for {peice} is {list} with a bid of {final[list]}$.")  # Display the winner

    else:
        print(f"It is a draw with a bid of {draw[list]} and the bidders are:")  # Inform about a draw
        for list in draw:
            print(f"{list}")  # Display bidders involved in the draw

    # Ask if the user wants to bid again
    yes = input("Do you want to Bid again?:\n'Yes' or 'no'")

    if yes == 'yes':
        again = True  # Restart the bidding process
        os.system('cls')  # Clear the screen
        
    else:
        again = False  # End the bidding process
        os.system('cls')  # Clear the screen

print("Thank you for Bidding and GoodBye!")  # Bid farewell message
input("Tap Enter to Exit!")  # Wait for user input before exiting the program
