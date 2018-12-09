"""
Advent of code 2016 - Day 20, Part 1

Firewall Rules
===

You'd like to set up a small hidden computer here so you can use it to get
back into the network later. However, the corporate firewall only allows
communication with certain external IP addresses.

You've retrieved the list of blocked IPs from the firewall, but the list seems
to be messy and poorly maintained, and it's not clear which IPs are allowed.
Also, rather than being written in dot-decimal notation, they are written as
plain 32-bit integers, which can have any value from 0 through 4294967295,
inclusive.

For example, suppose only the values 0 through 9 were valid, and that you
retrieved the following blacklist:

5-8
0-2
4-7

The blacklist specifies ranges of IPs (inclusive of both the start and end
value) that are not allowed. Then, the only IPs that this firewall allows
are 3 and 9, since those are the only numbers not in any range.

Given the list of blocked IPs you retrieved from the firewall (your puzzle
input), what is the lowest-valued IP that is not blocked?
"""
import fileinput, doctest

def parse_line(line): return tuple(map(int, line.split('-')))

def sub(r1, r2):
    """ Subtract range r1 from range r2 from another
    >>> sub((3, 4), (1, 3))
    [(1, 2)]
    >>> sub((1, 2), (2, 4))
    [(3, 4)]
    >>> sub((4, 4), (1, 3))
    [(1, 3)]
    >>> sub((1, 1), (2, 4))
    [(2, 4)]
    >>> sub((2, 3), (1, 4))
    [(1, 1), (4, 4)]
    """
    res = []
    if r2[0] < r1[0] <= r2[1]:
        res.append((r2[0], r1[0] - 1))
    if r2[0] <= r1[1] < r2[1]:
        res.append((r1[1] + 1, r2[1]))
    return res if res else [r2]

def whitelist(_range, blacklist):
    return reduce(lambda acc, b: [i for a in acc for i in sub(b, a)], 
                  sorted(map(parse_line, blacklist)), [_range])

if __name__ == '__main__':
    doctest.testmod()
    print whitelist((0, 4294967295), [x.strip() for x in fileinput.input()])[0][0]
