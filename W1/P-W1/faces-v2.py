# Use def main function
# Ask user for input
def main():
    statement = ""
    print(convert(statement))
    

# Use def to create convert function
def convert(to):
    return input("Type Message: ").replace(":)", "🙂").replace(":(", "🙁")

main()
