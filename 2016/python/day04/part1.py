"""
Advent of code 2016 - Day 4, Part 1

Security Through Obscurity
===

Finally, you come across an information kiosk with a list of rooms. Of course,
the list is encrypted and full of decoy data, but the instructions to decode
the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes)
followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in
the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a
(5), b (3), and then a tie between x, y, and z, which are listed
alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all
tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
import re
import fileinput
from collections import Counter

digits = re.compile(r'\d+')

def count_alpha(tupl):
    return 128 * tupl[1] - ord(tupl[0])

def compute_hash(string):
    return "".join([x[0] for x in reversed(
        sorted(Counter(string).most_common(), key=count_alpha))])[:5]

def valid(line):
    name, _hash = digits.split(line.strip())
    return compute_hash(name.replace('-', '')) == _hash[1:-1]

def secure_obscurity(ls):
    return sum(int(digits.search(l.strip()).group(0)) for l in ls if valid(l))

assert secure_obscurity(["aaaaa-bbb-z-y-x-123[abxyz]"]) == 123
assert secure_obscurity(["a-b-c-d-e-f-g-h-987[abcde]"]) == 987
assert secure_obscurity(["not-a-real-room-404[oarel]"]) == 404
assert secure_obscurity(["totally-real-room-200[decoy]"]) == 0


if __name__ == '__main__':
    print secure_obscurity(fileinput.input())
