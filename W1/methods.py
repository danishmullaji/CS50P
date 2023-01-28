# Ask user for the input
name = input("Tell me your full name: ")

# Method: It remove the blank spaces typed by the user
name = name.strip()

# Method: It capitalize the first letter of the input
name = name.capitalize()

# Method: It capitalize the first letter of all the words mentioned of the input
name = name.title()

# Method: It split the string into short substring and it can be use separately 
first, last = name.split()

# Method: It replace the provided value with the assigned value
name = name.replace(" ", "...")

# Method: It round-off the numbers to the nearest value
digit_one = 1010.59
digit_two = 1010.64

summation = round(digit_one + digit_two, 2)

# Use print function
print(f"Hello, {first}")
print(f"Total: {summation:,}")
