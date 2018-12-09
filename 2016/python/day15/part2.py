"""
Advent of code 2016 - Day 15, Part 2

Timing is Everything
===
After getting the first capsule (it contained a star! what great fortune!),
the machine detects your success and begins to rearrange itself.

When it's done, the discs are back in their original configuration as if it
were time=0 again, but a new disc with 11 positions and starting at position
0 has appeared exactly one second below the previously-bottom disc.

With this new disc, and counting again starting from time=0 with the
configuration in your puzzle input, what is the first time you can press
the button to get another capsule?
"""
import fileinput
from part1 import solve

if __name__ == '__main__':
    print solve([x.strip() for x in fileinput.input()] + [
        'Disc #7 has 11 positions; at time=0, it is at position 0.'])

