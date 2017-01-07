"""
Advent of code 2016 - Day 4, Part 1

Security Through Obscurity
===

With all the decoy data out of the way, it's time to decrypt this list and get
moving.

The room names are encrypted by a state-of-the-art shift cipher, which is
nearly unbreakable without the right software. However, the information kiosk
designers at Easter Bunny HQ were not expecting to deal with a master
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a
number of times equal to the room's sector ID. A becomes B, B becomes C, Z
becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""
import re
import fileinput
from collections import Counter
from part1 import digits, compute_hash

A = ord('a')

def secure_obscurity(lines):
    decrypted_lines = []

    for line in lines:
        name, _hash = digits.split(line.strip())
        if compute_hash(name.replace('-', '')) == _hash[1:-1]:
            sector = int(digits.search(line.strip()).group(0))

            decrypted = "".join(
                " " if l == '-' else chr((ord(l) - A + sector) % 26 + A)
                for l in name)
            decrypted_lines.append(
                "\"{}\" {}".format(decrypted.strip(), sector))

    return "\n".join(decrypted_lines)

assert secure_obscurity(["qzmt-zixmtkozy-ivhz-343[zimth]"]) == \
    "\"very encrypted name\" 343"

if __name__ == '__main__':
    print secure_obscurity(fileinput.input())
