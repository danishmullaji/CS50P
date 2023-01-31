def main():
    # Ask user input for two variables and operator 
    x = float(input("Value for x?: "))
    y = float(input("Value for y?: "))
    z = input("Choose an operator: ")
    cal(x, z, y)


# Use print function with f-string to convert value into financial
def cal(v1, v2, v3):
    if v2 == "+":
        print(f"{v1 + v3:,.2f}")
    elif v2 == "-":
        print(f"{v1 - v3:,.2f}")
    elif v2 == "*":
        print(f"{v1 * v3:,.2f}")
    elif v2 == "/":
        print(f"{v1 / v3:,.2f}")


main()
