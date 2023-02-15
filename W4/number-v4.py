def main():
    x = value()
    print(f"value of x is {x}")


def value():
    while True:
        try:
            x = int(input("Enter x: "))
        except ValueError:
            print("x is not an integer")
        else:
            break

    return x


main()