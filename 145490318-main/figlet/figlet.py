import sys
import random
from pyfiglet import Figlet

def get_font(argv):
    if len(argv) == 0:
        return None
    elif len(argv) == 2 and (argv[0] == '-f' or argv[0] == '--font'):
        return argv[1]
    else:
        print("Invalid command-line arguments.")
        sys.exit(1)

def get_figlet(font):
    figlet = Figlet(font=font)
    return figlet

def get_random_font():
    figlet = Figlet()
    fonts = figlet.getFonts()
    random_font = random.choice(fonts)
    return random_font

def main(argv):
    font = get_font(argv)

    if font is None:
        random_font = get_random_font()
        figlet = get_figlet(random_font)
    else:
        figlet = get_figlet(font)

    user_input = input("Enter a string of text: ")
    print(figlet.renderText(user_input))

if __name__ == "__main__":
    main(sys.argv[1:])
