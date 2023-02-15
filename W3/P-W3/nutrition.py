nutrition = {
    "apple" : "130",
    "avocado" : "50",
    "banana" : "110",
    "cantaloupe" : "50",
    "grapefruit" : "60",
    "grapes" : "90",
    "honeydewmelon" : "50",
    "kiwifruit" : "90",
    "sweetcherries" : "100"
}

fruit = input("Item: ").lower().strip()

if fruit in nutrition:
    print(f"Calories: {nutrition[fruit]}")
