import sys

if len(sys.argv) < 2:
    sys.exit("Mention your name while running file")

for name in sys.argv[1:]:
    print(f"Hello, {name}")