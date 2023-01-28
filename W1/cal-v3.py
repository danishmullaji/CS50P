# Ask user input and nest with integer
x = float(input("What's x? "))
y = float(input("What's y? "))

# Use round function to round-off the value
# Method: It rounds to nearest integer
# round(number [, ndigits]) - ndigit is option and you can custom the rounds value.
z = round(x + y, 1)

# Convert numbers into financial values
print(f"Total value: {z:,}")
