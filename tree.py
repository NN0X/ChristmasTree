from math import log
from time import sleep
from random import random, choice
from argparse import ArgumentParser

DARKGREEN = "\033[32m"
BLUE = "\033[94m"
RED = "\033[91m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
BROWN = "\033[33m"
RESET = "\033[0m"
CLEAR = "\033c"
DECORATIONCOLORS = [RED, BLUE, MAGENTA, CYAN]
DECORATIONS = ["@", "O", "+", "x"]

def gentree(basewidth=25, steps=30):
    tree = DARKGREEN
    scale = basewidth / steps
    for i in range(1, steps + 1):
        width = int(i * scale)
        if width % 2 != 0:
            width -= 1
        maxwidth = basewidth - width
        emptywidth = maxwidth // 2
        if width == 2:
            tree+=YELLOW + " "*emptywidth + "*"*width + DARKGREEN + "\n"
        else:
            tree+=" "*emptywidth + "#"*width + "\n"

    tree += BROWN
    tree += (" "*((basewidth - 4) // 2) + "||||\n")*2

    return tree

def decorate(tree, basewidth=25, probability=0.4):
    decorated = ""
    for c in tree:
        if c == '#' and random() < probability:
            decorated+=choice(DECORATIONCOLORS) + choice(DECORATIONS) + DARKGREEN
        else:
            decorated+=c

    return decorated

def animate(tree, delay=0.5):
    animated = tree
    while True:
        animated = (
            animated
            .replace(RED, "__TMP__")
            .replace(BLUE, RED)
            .replace("__TMP__", BLUE)
            .replace(MAGENTA, "__TMP__")
            .replace(CYAN, MAGENTA)
            .replace("__TMP__", CYAN)
        )

        print(CLEAR + animated + RESET)
        sleep(delay)

def main(basewidth, steps, probability, delay):
    tree = gentree(basewidth, steps)
    christmastree = decorate(tree, basewidth, probability)
    animate(christmastree, delay)

if __name__ == "__main__":
    parser = ArgumentParser(description="Christmas tree.")
    parser.add_argument("-b", "--basewidth", type=int, default=25, help="Width of the tree base")
    parser.add_argument("-s", "--steps", type=int, default=30, help="Number of generation steps")
    parser.add_argument("-p", "--probability", type=float, default=0.4, help="Probability to place a decoration")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Delay between animation frames [seconds]")
    args = parser.parse_args()
    try:
        main(args.basewidth, args.steps, args.probability, args.delay)
    except KeyboardInterrupt:
        print(CLEAR + RESET)
        print("Merry Christmas!")
