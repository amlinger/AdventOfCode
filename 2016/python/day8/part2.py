"""
Advent of code 2016 - Day 8, Part 2

Two-Factor Authentication
===

You notice that the screen is only capable of displaying capital letters;
in the font it uses, each letter is 5 pixels wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
"""
import fileinput
from part1 import interpret

def pixel_str(pixel):
    return "\033[100m{} \033[0m".format('\033[93m#' if pixel else '\033[2m.')
def LED_draw(LED):
    return "\n".join(map(
        lambda row: "".join([pixel_str(pixel) for pixel in row]), LED))

if __name__ == '__main__':
    print LED_draw(interpret(fileinput.input()))
