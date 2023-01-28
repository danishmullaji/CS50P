# Ask user for an input
name = input("Tell me your full name: ")

# Method: It remove the blank spaces typed by the user
name = name.strip()

# Method: It capitalize the first letter of the input
name = name.capitalize()

# Method: It capitalize the first letter of all the words mentioned of the input
name = name.title()

# Method: It split the string into short substring and it can be use separately 
first, last = name.split()

# Use print function
print(f"Hello, {first}")
