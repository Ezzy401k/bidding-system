import os

again = True
while again:
    store = {}
    bidding = True
    peice = input("What are you Bidding on?:\n")
    while bidding:
        print(f"Welcome to the secret auction program for {peice}.")
        name = input("What is your name?:\n")
        bid = int(input("What's your bid?:\n$"))
        
        def bids(name,bid):
            store[name] = bid
            
        bids(name, bid)
        again = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
        if again == "yes":
            os.system('cls')
        else:
            bidding = False
            os.system('cls')
    final = {}
    draw = {}
    for items in store:
        if final == {}:
            final[items] = store[items]
            
        else:
            for list in final:
                if store[items] > final[list]:
                    final = {}
                    draw = {}
                    final[items] = store[items]
                elif store[items] == final[list]:
                    draw[items] = store[items]
                    draw[list] = final[list]

    if draw == {}:
        for list in final:
            print(f"The winner of bid for {peice} is {list} with a bid of {final[list]}$.")
    else:
        print(f"It is a draw with a bid of {draw[list]} and the bidders are:")
        for list in draw:
            print(f"{list}")

    yes = input("Do you want to Bid again?:\n'Yes' or 'no'")
    if yes == 'yes':
        again = True
        os.system('cls')
    else:
        again = False
        os.system('cls')
print("Thank you for Bidding and GoodBye!")
input("Tap Enter to Exit!")