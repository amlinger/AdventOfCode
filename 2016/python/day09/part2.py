"""
Advent of code 2016 - Day 9, Part 2

Explosives in Cyberspace
===

Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data
are decompressed. This, the documentation explains, provides much more
substantial compression capabilities, allowing many-gigabyte files to be stored
in only a few kilobytes.

For example:

(3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no
         markers.
X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data
                from the (8x2) marker is then further decompressed, thus
                triggering the (3x3) marker twice for a total of six ABC
                sequences.
(27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated
                                   241920 times.
(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445
                                                         characters long.
Unfortunately, the computer you brought probably doesn't have enough memory to
actually decompress the file; you'll have to come up with another way to get
its decompressed length.

What is the decompressed length of the file using this improved format?
"""
import fileinput

def next_index(data, ptr):
    i = data.index(')', ptr) + 1
    _len, rep = map(int, data[ptr:i - 1].split('x'))
    return (i + _len, explosives(data[:i + _len], i) * rep)

def explosives(data, ptr=0):
    if (ptr >= len(data)): return 0
    if data[ptr] != '(': return 1 + explosives(data, ptr + 1)

    ptr, _len = next_index(data, ptr + 1)
    return _len + explosives(data, ptr)

assert explosives('(3x3)XYZ') == len('XYZXYZXYZ')
assert explosives('X(8x2)(3x3)ABCY') == len('XABCABCABCABCABCABCY')
assert explosives('(27x12)(20x12)(13x14)(7x10)(1x12)A') == 241920
assert explosives('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN') \
    == 445

if __name__ == '__main__':
    print explosives("".join([x.strip() for x in fileinput.input()]))
