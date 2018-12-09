"""
Advent of code 2016 - Day 12, Part 2

Leonardo's Monorail
===
As you head down the fire escape to the monorail, you notice it didn't start;
register c needs to be initialized to the position of the ignition key.

If you instead initialize register c to be 1, what value is now left in
register a?
"""
import fileinput
from part1 import execute, Computer

if __name__ == '__main__':
    computer = Computer()
    computer.registers['c'] = 1
    execute([x.strip().lower() for x in fileinput.input()], computer)

