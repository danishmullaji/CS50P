while True:
    try:
        x = int(input("Enter x: "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"value of x is {x}")
