"""
Advent of code 2016 - Day 21, Part 2

Scrambled Letters and Hash
===

You scrambled the password correctly, but you discover that you can't actually
modify the password file on the system. You'll need to un-scramble one of the
existing passwords by reversing the scrambling process.

What is the un-scrambled version of the scrambled password fbgdceah?
"""
import fileinput
from itertools import permutations
from part1 import scramble 

# Brute force the unscrambling since password is only 8 characters long
# and has only 8 possible values...
def unscramble(target, instructions):
    for candidate in map(lambda p: "".join(p), permutations("abcdefgh")):
        if scramble(candidate, instructions) == target:
            return candidate

if __name__ == '__main__':
    print unscramble('fbgdceah', [x.strip() for x in fileinput.input()])

