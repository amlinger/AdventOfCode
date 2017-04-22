"""
Advent of code 2016 - Day 3, Part 1

Squares With Three Sides
===

Now that you can think clearly, you move deeper into the labyrinth of hallways
and office furniture that makes up this part of Easter Bunny HQ. This must be
a graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes,
but... 5 10 25? Some of these aren't triangles. You can't help but mark the
impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining
side. For example, the "triangle" given above is impossible, because 5 + 10 is
not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""
import fileinput

def valid_triangle(x, y, z):
    return max(x, max(y, z)) * 2 < (x + y + z)

def valid_triangle_line(line):
    return valid_triangle(*map(int, line.strip().split()))

def three_sides(description):
    return sum([int(valid_triangle_line(line)) for line in description])

# Sanity check
assert valid_triangle_line("5 10 25") == False
assert valid_triangle_line("5 5 5") == True

if __name__ == '__main__':
    print three_sides(fileinput.input())
