# Use while loop
while True:
    try:
        # Ask user input for x and y
        x, y = input("Fraction: ").split("/")
        # Covert the str to int for calculation
        percent = (int(x) * 100) / int(y)

        # Use if elif else statement
        if percent > 100:
            continue
        elif 98 >= percent >= 2:
            print(f"{percent:.0f}%")
        elif percent >= 99:
            print("F")
        else:
            print("E")

# Check for ValueError and ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        pass
    else:
        break
