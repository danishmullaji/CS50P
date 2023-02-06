# Ask user input for three variable
x, y, z = input().split()

# Use if elif else statement for calculation
if y == "+":
    sum = int(x) + int(z)
    print(float(sum))
elif y == "-":
    print(float(int(x) - int(z)))
elif y == "*":
    print(float(int(x) * int(z)))
elif y == "/":
    print(float(int(x) / int(z)))
else:
    print("ERROR")
