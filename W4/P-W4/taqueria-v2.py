menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

# Use while loop
while True:
    try:
        # Ask user input for order
        order = input("Item: ").title()

        for food in menu:
            if order == food:
                # Add up all the order until user press blank
                total = total + menu[order]
                # Show the total amount
                print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break
