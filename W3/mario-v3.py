# Create main function and use def block function
def main():
    block(3)


# Create def block function using for loop
def block(size):
    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()


main()