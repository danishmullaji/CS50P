import sys

if len(sys.argv) < 2:
    sys.exit("Mention your name while running file")
elif len(sys.argv) > 2:
    sys.exit("If mentioning your fullname use \"\"")

print(f"Hello, {sys.argv[1]}")

"""try:
    print(f"Hello, {sys.argv[1]}")
except IndexError:
    print("Mention your name while running file")"""