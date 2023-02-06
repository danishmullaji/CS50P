# Ask user input and make input case sensitive
life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower()

# Use if else statement to solve
if life == "forty two" or life == "42" or life == "forty-two":
    print("Yes")
else:
    print("No")