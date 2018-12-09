"""
Advent of code 2016 - Day 21, Part 1

Scrambled Letters and Hash
===

The computer system you're breaking into uses a weird scrambling function to
store its passwords. It shouldn't be much trouble to create your own scrambled
password so you can add it to the system; you just have to implement the
scrambler.

The scrambling function is a series of operations (the exact list is provided
in your puzzle input). Starting with the password to be scrambled, apply each
operation in succession to the string. The individual operations behave as
follows:

    swap position X with position Y means that the letters at indexes X and Y
        (counting from 0) should be swapped.
    swap letter X with letter Y means that the letters X and Y should be
        swapped (regardless of where they appear in the string).
    rotate left/right X steps means that the whole string should be rotated;
        for example, one right rotation would turn abcd into dabc.
    rotate based on position of letter X means that the whole string
        should be rotated to the right based on the index of letter X
        (counting from 0) as determined before this instruction does any
        rotations. Once the index is determined, rotate the string to the
        right one time, plus a number of times equal to that index, plus one
        additional time if the index was at least 4.
    reverse positions X through Y means that the span of letters at indexes X
        through Y (including the letters at X and Y) should be reversed in
        order.
    move position X to position Y means that the letter which is at index X
        should be removed from the string, then inserted such that it ends up
        at index Y.

For example, suppose you start with abcde and perform the following operations:

    swap position 4 with position 0 swaps the first and last letters,
        producing the input for the next step, ebcda.
    swap letter d with letter b swaps the positions of d and b: edcba.
    reverse positions 0 through 4 causes the entire string to be reversed,
        producing abcde.
    rotate left 1 step shifts all letters left one position, causing the first
        letter to wrap to the end of the string: bcdea.
    move position 1 to position 4 removes the letter at position 1 (c), then
        inserts it at position 4 (the end of the string): bdeac.
    move position 3 to position 0 removes the letter at position 3 (a), then
        inserts it at position 0 (the front of the string): abdec.
    rotate based on position of letter b finds the index of letter b (1), then
        rotates the string right once plus a number of times equal to that
        index (2): ecabd.
    rotate based on position of letter d finds the index of letter d (4), then
        rotates the string right once, plus a number of times equal to that
        index, plus an additional time because the index was at least 4, for a
        total of 6 right rotations: decab.

After these steps, the resulting scrambled password is decab.

Now, you just need to generate a new scrambled password and you can access
the system. Given the list of scrambling operations in your puzzle input, what
is the result of scrambling abcdefgh?
"""
import fileinput, doctest, re

def swap(s, l, r): 
    """ Swap the place of index l and r in string s

    >>> swap('abc', '0', '2')
    'cba'
    >>> swap('abc', '1', '2')
    'acb'
    >>> swap('abc', '2', '1')
    'acb'
    >>> swap('abc', 'c', 'b')
    'acb'
    >>> swap('abc', 'b', 'c')
    'acb'
    """
    try:
        r, l = [int(r), int(l)]
    except ValueError:
        r, l = [s.index(r), s.index(l)]
    return "".join(
            s[r] if l == i else s[l] if r == i else s[i] for i in range(len(s)))

def reverse(s, start, stop):
    """ Reverses s with the inclusive range given

    >>> reverse('abcd', '2', '3')
    'abdc'
    >>> reverse('abcd', '1', '2')
    'acbd'
    >>> reverse('abcd', '0', '3')
    'dcba'
    """
    start, stop = [int(start), int(stop)]
    return s[:start] + "".join(reversed(s[start:stop+1])) + s[stop+1:]

def rotate(s, *args):
    """ Rotates the string in various fashions

    >>> rotate('abc', 'right', '1')
    'cab'
    >>> rotate('abc', 'right', '2')
    'bca'
    >>> rotate('abc', 'left', '1')
    'bca'
    >>> rotate('abc', 'left', '2')
    'cab'
    >>> rotate('abc', 'a')
    'cab'
    >>> rotate('ecabd', 'd')
    'decab'
    """
    if len(args) == 1:
        idx = s.index(args[0]) 
        l, _dir, i = [len(s), 'right', idx + 1 if idx < 4 else idx + 2]
    else:
        l, _dir, i = [len(s), args[0], int(args[1])]
    if _dir == 'right':
        return s[-i%l:] + s[:-i%l]
    return s[i%l:] + s[:i%l]

def move(s, *args):
    """ Move character at position from f to t

    >>> move('bcdea', '1', '4')
    'bdeac'
    """
    f, t = map(int, args)
    tmp = s[:f] + s[f+1:]
    return tmp[:t] + s[f] + tmp[t:]

INST = {'swap': swap, 'reverse': reverse, 'rotate': rotate, 'move': move}

def arguments(instruction):
    return re.findall(r'(left|right|\d+|(?<=letter )[a-z]+)', instruction)

def exec_instr(prev, i):
    return INST[i.split(' ')[0]](prev, *arguments(i))

def scramble(inp, instructions):
    return reduce(exec_instr, instructions, inp)

if __name__ == '__main__':
    doctest.testmod()
    print scramble('abcdefgh', (x.strip() for x in fileinput.input()))

