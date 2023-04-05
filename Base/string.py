# print function help providing an output
print("Python")

# variables act as an container which holds the value, It can be pre-determined value or user generated
greetings = "Welcome to learning python"
name = "Danish"

# we can concatenate the string using the plus sign, which means we add two or  more string togther in one line
output = greetings + ", " + name

# other method to add up multiple string is to use func format
output = "{}, {}".format(greetings, name)

# or else we can use func f-string introducted in v3.6, Where you can input the variable while formatting it.
output = f"{greetings}, {name}"

print(output)

print()

print("What is Python?")
py = """Python is a computer programming language often used to build websites and software, automate tasks, and conduct data analysis.
Python is a general-purpose language, meaning it can be used to create a variety of different programs and isn’t specialized for any specific problems. 
This versatility, along with its beginner-friendliness, has made it one of the most-used programming languages"""

# func len help you find the length of the string
print(len(py))

# func count help you count the letter or words mentioned in the string
print(py.count("Python"))

# method slicing is use to move around and slice the string
# if we move outside the string index we get negative output
# keeping prefix or suffix blank means start or till the end
print(py[:41])
