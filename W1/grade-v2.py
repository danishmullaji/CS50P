# Ask User input
score = int(input("Enter your score: "))

# Write condition for if and elif
if 75 <= score <= 100:
    print("Grade: A - Excellent")
elif 60 <= score < 75:
    print("Grade: B - Satisfactory")
elif 45 <= score < 60:
    print("Grade: C - Good")
elif 35 <= score < 45:
    print("Grade: D - Poor")
else:
    print("Grade: F - Fail")
