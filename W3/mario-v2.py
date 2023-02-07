# Create def main 
def main():
    size = int(input("Enter brick size: "))
    row(size)
    column(size)


# Create def row function
def row(brick):
    for _ in range(brick):
        print("#")

# Create def column function
def column(brick):
    print("#" * brick)


main()