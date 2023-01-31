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
# Line 15: return True if number % 2 == 0 else return False
def even(number):
    return number % 2 == 0


main()
