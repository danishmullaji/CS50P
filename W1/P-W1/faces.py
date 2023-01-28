# Use def main function
# Use print function with created convert function
def main():
    statement = ""
    print(convert(statement))

# Use def to create convert function
def convert(to):
    to = input("Type Message: ").replace(":)", "🙂").replace(":(", "🙁")
    return to

main()
