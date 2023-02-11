# Ask user input
tweet = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]

# Replace vowels with nothing
for twt in tweet:
    if twt in vowels:
        tweet = tweet.replace(twt, "")

print(f"Output: {tweet}")
