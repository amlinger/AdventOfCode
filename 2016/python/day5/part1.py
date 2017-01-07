"""
Advent of code 2016 - Day 5, Part 1

How About a Nice Game of Chess?
===

You are faced with a security door designed by Easter Bunny engineers that seem
to have acquired most of their security knowledge by watching hacking movies.

The eight-character password for the door is generated one character at a time
by finding the MD5 hash of some Door ID (your puzzle input) and an increasing
integer index (starting with 0).

A hash indicates the next character in the password if its hexadecimal
representation starts with five zeroes. If it does, the sixth character in the
hash is the next character of the password.

For example, if the Door ID is abc:

The first index which produces a hash that starts with five zeroes is 3231929,
which we find by hashing abc3231929; the sixth character of the hash, and thus
the first character of the password, is 1.
5017308 produces the next interesting hash, which starts with 000008f82..., so
the second character of the password is 8.
The third time a hash starts with five zeroes is for abc5278568, discovering
the character f.
In this example, after continuing this search a total of eight times, the
password is 18f47a30.

Given the actual Door ID, what is the password?

Your puzzle input is ojvtpuvg.
"""
import sys
import md5
from itertools import count

def get_password(door_id):
    pwd = ""
    for i in count(start=1, step=1):
        hashed = md5.new("{}{}".format(door_id, i)).hexdigest()
        if hashed.startswith("0" * 5):
            pwd = pwd + hashed[5]
            if len(pwd) >= 8:
                return pwd

# Very time-consuming sanity-check:
assert get_password('abc') == "18f47a30"

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python part1.py <door_id>"
    print get_password(sys.argv[1])
