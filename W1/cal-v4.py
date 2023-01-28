# Ask user input and nest with integer
x = float(input("What's x? "))
y = float(input("What's y? "))

# Use fstring to remove round function and convert digits into financial numbers 
print(f"{x + y:,.2f}")
