# Ask user input for three variable
x, y, z = input().split()

# Use match condition for calculation
match y:
    case "+":
        print(f"{int(x) + int(z):,}")
    case "-":
        print(f"{int(x) - int(z):,}")
    case "*":
        print(f"{int(x) * int(z):,}")
    case "/":
        print(f"{int(x) / int(z):,}")
    case _:
        print("ERROR")
