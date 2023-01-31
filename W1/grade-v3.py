# Ask User input
score = int(input("Enter your score: "))

# Write condition for if and elif
if score >= 90:
    print("Grade: A - Excellent")
elif score >= 75:
    print("Grade: B - Satisfactory")
elif score >= 60:
    print("Grade: C - Good")
elif score >= 35:
    print("Grade: D - Poor")
else:
    print("Grade: F - Fail")
