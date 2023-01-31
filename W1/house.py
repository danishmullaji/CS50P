name = input("Your name? ")

# Use match condition
match name:
    case "Harry" | "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Luna":
        print("Ravenclaw")
    case _:
        print("Who?")