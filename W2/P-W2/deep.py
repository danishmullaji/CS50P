# Ask user input
life = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Use match function
match life:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
