# Ask user input
# input either 25, 10, 5 else reprompt
# add up the amount show the remaining amount

due = 50

while True:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))

    if coin > due and coin == 25:
        due = due - (coin - 20)
        print(f"Change Owed: {due}")
        break

    if coin == 25 or coin == 10 or coin == 5:
        due = due - coin

# continue taking the input until 50 reached
    if due > 0:
        continue
    else:
        print(f"Change Owed: {due}")
        break
