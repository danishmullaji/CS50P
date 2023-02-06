# Create def main with def get_repeat and meow
def main():
    number = get_repeat()
    meow(number)

# Create def get_repeat
def get_repeat():
    while True:
        n = int(input("What is n? "))
        if n > 0:
            return n

# Create def meow
def meow(n):
    for _ in range(n):
        print("Meow")


main()