# prompt user for the initial ilamas
initial = int(input("Currently how many ilamas: "))

# prompt user for the future ilamas
final = int(input("What will be the goal to reach: "))

# calculate were 3 are born and 4 dies
# print the years it will take to reach the goal
years = 0
while initial < final:
    initial = initial + (initial / 3) - (initial / 4)
    years += 1
    continue

print(f"Total years it will take to reach is {years}")
