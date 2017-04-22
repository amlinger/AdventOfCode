"""
Advent of code 2016 - Day 3, Part 2

Squares With Three Sides
===

Now that you've helpfully marked up their design documents, it occurs to you
that triangles are specified in groups of three vertically. Each set of three
numbers in a column specifies a triangle. Rows are unrelated.

For example, given the following specification, numbers with the same hundreds
digit would be part of the same triangle:

101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603
In your puzzle input, and instead reading by columns, how many of the listed
triangles are possible?
"""
import fileinput
from part1 import three_sides

# We simply transform the input we recieve, by reading lines in chunks of 3,
# and picking values vertically instead of horizontally.
def reverser(d):
    try:
        while True:
            rows = [row.strip().split() for row in [next(d), next(d), next(d)]]
            for i in range(3):
                yield "{} {} {}".format(rows[0][i], rows[1][i], rows[2][i])
    except StopIteration:
        pass # We ran out of input and must be done.


if __name__ == '__main__':
    print three_sides(reverser(fileinput.input()))
