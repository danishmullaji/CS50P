# Ask User input
score = int(input("Enter your score: "))

# Write condition for if and elif
if score >= 75 and score <=100:
    print("Grade: A - Excellent")
elif score >= 60 and score < 75:
    print("Grade: B - Satisfactory")
elif score >= 45 and score < 60:
    print("Grade: C - Good")
elif score >=35 and score < 45:
    print("Grade: D - Poor")
else:
    print("Grade: F - Fail")