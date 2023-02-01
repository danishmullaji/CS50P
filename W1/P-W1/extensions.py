# Ask user input
file = input("Upload the file: ").strip().lower()

# Create if elif else statement
if file.endswith(".jpeg"):
    print("image/jpeg")
elif file.endswith(".jpg"):
    print("image/jpeg")
elif file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
