# Ask user input
file, type = input("Enter file: ").split(".")

# Use if elif else statement to solve
if type == "jpeg" or type == "jpg":
    print("image/jpeg")
elif type == "gif":
    print("image/gif")
elif type == "png":
    print("image/png")
elif type == "pdf":
    print("application/pdf")
elif type == "txt":
    print("text/plain")
elif type == "zip":
    print("application/zip")
else:
    print("application/octet-stream")