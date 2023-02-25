from pyfiglet import Figlet
import random
import sys

figlet = Figlet()

if len(sys.argv) <= 1:
    word = input("Input: ")
    font = Figlet(font = random.choice(figlet.getFonts()))
    print(font.renderText(word))


elif len(sys.argv) <= 3:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        word = input("Input: ")
        font = Figlet(font = sys.argv[2])
        print(font.renderText(word))
    else:
        print("Invalid usage")
