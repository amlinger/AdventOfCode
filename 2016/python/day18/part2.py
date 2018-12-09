"""
Advent of code 2016 - Day 18, Part 2

Like a Rogue
===

How many safe tiles are there in a total of 400000 rows?
"""
import fileinput
from part1 import gen_field, read_row

if __name__ == '__main__':
    assert sum(map(sum, gen_field(read_row('.^^.^.^^^^'), 10))) == 38
    print sum(map(sum, gen_field(read_row(next(fileinput.input())), 400000)))

