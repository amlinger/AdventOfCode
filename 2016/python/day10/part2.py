"""
Advent of code 2016 - Day 10, Part 2

Balance Bots
===
What do you get if you multiply together the values of one chip in each of
outputs 0, 1, and 2?
"""
import fileinput
from part1 import parse_lines

def balance_bots(lines):
    bots, output = parse_lines(lines)

    one, two, three = [output[i]() for i in ['0', '1', '2']]
    print "The product of 0, 1 and 2 output bins is {} * {} * {} = {}".format(
            one, two, three, one * two * three)

if __name__ == '__main__':
    balance_bots(x.strip() for x in fileinput.input())

