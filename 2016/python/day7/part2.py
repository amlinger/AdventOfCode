"""
Advent of code 2016 - Day 7, Part 2

Internet Protocol Version 7
===

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in
the supernet sequences (outside any square bracketed sections), and a
corresponding Byte Allocation Block, or BAB, anywhere in the hypernet
sequences. An ABA is any three-character sequence which consists of the same
character twice with a different character between them, such as xyx or aba. A
corresponding BAB is the same characters but in reversed positions: yxy and
bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab
within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet;
the aaa sequence is not related, because the interior character must be
different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a
corresponding bzb, even though zaz and zbz overlap).

How many IPs in your puzzle input support SSL?
"""
import re
import fileinput
from part1 import no_brackets_re, brackets_re

def is_aba(test): return test[0] == test[2] and test[0] != test[1]
def flip_aba(aba): return "{b}{a}{b}".format(a=aba[0], b=aba[1])
def get_abas(test):
    return filter(is_aba, [test[x:x+3] for x in range(len(test)-2)])

def ipv7_ssl_enabled(ip):
    bab_cands = map(flip_aba, sum(map(get_abas, no_brackets_re.split(ip)), []))
    return any([c in h for c in bab_cands for h in brackets_re.findall(ip)])

# Sanity check
assert ipv7_ssl_enabled("aba[bab]xyz")
assert not ipv7_ssl_enabled("xyx[xyx]xyx")
assert ipv7_ssl_enabled("aaa[kek]eke")
assert ipv7_ssl_enabled("zazbz[bzb]cdb")

if __name__ == '__main__':
    print sum([int(ipv7_ssl_enabled(x.strip())) for x in fileinput.input()])
