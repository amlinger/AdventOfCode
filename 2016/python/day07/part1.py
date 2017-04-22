"""
Advent of code 2016 - Day 7, Part 1

Internet Protocol Version 7
===

While snooping around the local network of EBHQ, you compile a list of IP
addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to
figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair of two
different characters followed by the reverse of that pair, such as xyyx or abba.
However, the IP also must not have an ABBA within any hypernet sequences, which
are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even
though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters
must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though
it's within a larger string).

How many IPs in your puzzle input support TLS?
"""
import re
import fileinput

no_brackets_re = re.compile(r'\[[a-z]+\]')
brackets_re    = re.compile(r'\[([a-z]+)\]')

def is_abba(test):
    return test[0] == test[3] and test[1] == test[2] and test[0] != test[1]

def abba_inside(test):
    return len(test) >= 4 and \
        any([is_abba(test[x:x + 4]) for x in range(len(test) - 3)])

def ipv7_tls_enabled(ip):
    return (not any(map(abba_inside, brackets_re.findall(ip)))) and \
           any(map(abba_inside, no_brackets_re.split(ip)))

# Sanity check
assert ipv7_tls_enabled("abba[mnop]qrst")
assert not ipv7_tls_enabled("abcd[bddb]xyyx")
assert not ipv7_tls_enabled("aaaa[qwer]tyui")
assert ipv7_tls_enabled("ioxxoj[asdfgh]zxcvbn")

if __name__ == '__main__':
    print sum([int(ipv7_tls_enabled(x.strip())) for x in fileinput.input()])
