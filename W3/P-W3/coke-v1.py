# Ask user input55
# input either 25, 10, 5 else reprompt
# add up the amount show the remaining amount

due = 50

while True:
    coin = int(input("Insert the coin: "))

    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin     
        print(f"Change owes: {due}")

# continue taking the input until 50 reached
    if due > 0:
        continue

    break
