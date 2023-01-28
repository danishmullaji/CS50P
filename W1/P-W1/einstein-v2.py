# Create def main function
def main():
    Mass = int(input("Enter Mass in Kilograms: "))
    E(Mass)


# Create def E function
def E(M):
    return print(f"E = {(M * pow(300000000, 2))}")
    

main()
