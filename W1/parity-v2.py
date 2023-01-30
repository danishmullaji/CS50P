# Create def main function
# Ask user input
# Use even function with if else
def main():
    digit = int(input("Enter the number: "))
    if even(digit):
        print(f"{digit} is a even number")
    else:
        print(f"{digit} is an odd number")


# Create def even function
def even(number):
    if number % 2 == 0:
        return True


main()