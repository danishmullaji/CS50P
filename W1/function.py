# Create def main function
# Get user input
def main():
    name = input("Name please: ")
    hello(name)

    x = int(input("What is x? "))
    print("x square is", square(x))

# Create def hello function


def hello(to):
    print(f"Hello, {to}")

# Create def square function


def square(n):
    return n * n


main()
