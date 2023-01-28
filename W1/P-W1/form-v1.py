# Get users full name and strip while display
name = input("Enter your full name: ").title().strip()

# Use capitalize the input
first, last = name.split()

# Get users phone number
number = input("Enter your number: ")

# Get users address and capitalize the whole input
address = input("Enter your address: ").upper()

# Get users city, postal code and country
city = input("Enter your city: ").capitalize()
postal_code = input("Enter your postal code: ")
country = input("Enter your country: ").capitalize()

# print all the detials with start and greetings
print("Personal Information")
print(f"First name: {first}")
print(f"Last name: {last}")
print(f"Phone number: {number}")
print(f"Address: {address}")
print(f"City: {city}")
print(f"Postal code: {postal_code}")
print(f"Country: {country}")

print("Thank you!! our officer will visit soon") 
