def main():
    y = value("Enter y: ")
    print(f"value of y is {y}")


"""def value():
    while True:
        try:
            x = int(input("Enter x: "))
            break
        except ValueError:
            print("x is not an integer")

    return x"""


"""def value():
    while True:
        try:
            return int(input("Enter x: "))
        except ValueError:
            print("x is not an integer")"""


# using prompt for giving choice to user to choose variable name and input statement
def value(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()