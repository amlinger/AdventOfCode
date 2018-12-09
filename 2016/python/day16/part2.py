"""
Advent of code 2016 - Day 16, Part 2

Dragon Checksum
===
The second disk you have to fill has length 35651584. Again using the initial
state in your puzzle input, what is the correct checksum for this disk?

Your puzzle input is still 10001001100000001.
"""
from part1 import checksum, dragon

if __name__ == '__main__':
    print checksum(dragon("10001001100000001", 35651584))
