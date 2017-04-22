"""
Advent of code 2016 - Day 5, Part 2

How About a Nice Game of Chess?
===

As the door slides open, you are presented with a second door that uses a
slightly more inspired security mechanism. Clearly unimpressed by the last
version (in what movie is the password decrypted in order?!), the Easter Bunny
engineers have worked out a better solution.

Instead of simply filling in the password from left to right, the hash now also
indicates the position within the password to fill. You still look for hashes
that begin with five zeroes; however, now, the sixth character represents the
position (0-7), and the seventh character is the character to put in that
position.

A hash result of 000001f means that f is the second character in the password. U
se only the first result for each position, and ignore invalid positions.

For example, if the Door ID is abc:

The first interesting hash is from abc3231929, which produces 0000015...; so,
5 goes in position 1: _5______.
In the previous method, 5017308 produced an interesting hash; however, it is
ignored, because it specifies an invalid position (8).
The second interesting hash is at index 5357525, which produces 000004e...;
so, e goes in position 4: _5__e___.
You almost choke on your popcorn as the final character falls into place,
producing the password 05ace8e3.

Given the actual Door ID and this new method, what is the password? Be extra
proud of your solution if it uses a cinematic "decrypting" animation.

Your puzzle input is still ojvtpuvg.
"""
import sys
import md5
from itertools import count

def password_done(candidate):
    return '_' not in candidate

# Printing a cool animation while waiting for the
def print_password(pwd, step=0):
    rotator = ['\\','|','/','-','\\','|','/','-']
    sys.stdout.write("\rDECRYPTING [{}]".format(
        pwd.replace('_', rotator[step % 8])))
    sys.stdout.flush()

def get_password(door_id):
    pwd = "_" * 8
    for i in count(start=1, step=1):
        # Print every 100000 attempt to get an Ok time on the spinners
        if i % 100000 == 0: print_password(pwd, i / 100000)

        hashed = md5.new("{}{}".format(door_id, i)).hexdigest()
        if hashed.startswith('0' * 5):
            pos = int(hashed[5], 16)
            if pos < 8 and pwd[pos] == '_':
                pwd = pwd[:pos] + hashed[6] + pwd[pos + 1:]
                # Make sure that we always print the
                print_password(pwd, i / 100000)

            if password_done(pwd): return pwd

# Very time-consuming sanity-check:
assert get_password('abc') == "05ace8e3"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python part1.py <door_id>"
    get_password(sys.argv[1])
