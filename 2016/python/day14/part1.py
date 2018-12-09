"""
Advent of code 2016 - Day 14, Part 1

One-Time Pad
===

In order to communicate securely with Santa while you're on this mission,
you've been using a one-time pad that you generate using a pre-agreed
algorithm. Unfortunately, you've run out of keys in your one-time pad, and so
you need to generate some more.

To generate keys, you first get a stream of random data by taking the MD5 of a
pre-arranged salt (your puzzle input) and an increasing integer index
(starting with 0, and represented in decimal); the resulting MD5 hash should
be represented as a string of lowercase hexadecimal digits.

However, not all of these MD5 hashes are keys, and you need 64 new keys for
your one-time pad. A hash is a key only if:

    It contains three of the same character in a row, like 777. Only consider
    the first such triplet in a hash.

    One of the next 1000 hashes in the stream contains that same character
    five times in a row, like 77777.

Considering future hashes for five-of-a-kind sequences does not cause those
hashes to be skipped; instead, regardless of whether the current hash is a
key, always resume testing for keys starting with the very next hash.

For example, if the pre-arranged salt is abc:

    The first index which produces a triple is 18, because the MD5 hash of
    abc18 contains ...cc38887a5.... However, index 18 does not count as a key
    for your one-time pad, because none of the next thousand hashes (index 19
    through index 1018) contain 88888.
    The next index which produces a triple is 39; the hash of abc39 contains
    eee. It is also the first key: one of the next thousand hashes (the one at
    index 816) contains eeeee.
    None of the next six triples are keys, but the one after that, at index 92,
    is: it contains 999 and index 200 contains 99999.
    Eventually, index 22728 meets all of the criteria to generate the 64th key.

So, using our example salt of abc, index 22728 produces the 64th key.

Given the actual salt in your puzzle input, what index produces your 64th
one-time pad key?

Your puzzle input is qzyelonm.
"""
import md5, sys, re

def int_stream(): return xrange(0, sys.maxint)

def md5_stretch(cand, num):
    return reduce(lambda c, _: md5.new(c).hexdigest(), xrange(num), cand)

def find_nth_key(salt, stretch=1, nth=64, lookahead=1000):
    # Create a stream generating all hashes, and prepopulate the cache with
    # the first {lookahead} hashes
    hashes = (md5_stretch(salt+str(i), stretch) for i in int_stream())
    cache = dict(zip(range(lookahead), hashes))

    keys = []
    for i in int_stream():
        if len(keys) >= nth: return keys

        # Populate one more entry in the cache for each value we check, then
        # find which character the first triple contains. If none, then check
        # the next key.
        cache[i+lookahead] = next(hashes)
        try:
            triple = next(re.finditer(r"(\w)\1{2,}", cache[i])).group(0)[0]*5
        except StopIteration:
            continue

        # If the next {lookahead} entries contain 5 numbers of the same 
        # character, it is a key and we will save it as such.
        if any((triple in cache[x]) for x in xrange(i+1, i+lookahead+1)):
            keys.append((i, cache[i]))
    return keys

if __name__ == '__main__':
    print find_nth_key('qzyelonm')
