# Create list with dict
houses = [
    {"house" : "Stark", "name" : "Jon", "segil" : "Direwolf"},
    {"house": "Lannister", "name": "Cersi", "segil": "Lion"},
    {"house": "Targaryen", "name": "Danerys", "segil": "Three head dragon"}
]

# Use for loop to display
for house in houses:
    print( house["house"], house["name"], house["segil"], sep=" - ")
