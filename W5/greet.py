# We can run the program without main() while only calling def created function
def main():
    user = input("Type your name: ")
    hello(user)
    goodbye(user)

def hello(x):
    print(f"Hello, {x}")

def goodbye(x):
    print(f"Goodbye, {x}")

# __name__ helps in preventing running the main() while imported
if __name__ == "__main__":
    main()
