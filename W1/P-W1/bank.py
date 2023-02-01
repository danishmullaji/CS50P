# Ask user input
greet = input("Hello...").strip()

# Create if elif else statement 
# Use print function
if greet.startswith("hello") or greet.startswith("Hello"):
    print("$0")
elif greet.startswith("h") or greet.startswith("H"):
    print("$20")
else:
    print("$100")
