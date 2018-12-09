"""
Advent of code 2016 - Day 20, Part 2

Firewall Rules
===

How many IPs are allowed by the blacklist?
"""
import fileinput
from part1 import whitelist

if __name__ == '__main__':
    print reduce(lambda s, r: s + 1 + r[1] - r[0], 
        whitelist((0, 4294967295), [x.strip() for x in fileinput.input()]), 0)
