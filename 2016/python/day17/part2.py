"""
Advent of code 2016 - Day 17, Part 2

Two Steps Forward
===
You're curious how robust this security solution really is, and so you decide
to find longer and longer paths which still provide access to the vault. You
remember that paths always end the first time they reach the bottom-right
room (that is, they can never pass through it, only end in it).

For example:

    If your passcode were ihgpwlah, the longest path would take 370 steps.
    With kglvqrro, the longest path would be 492 steps long.
    With ulqzkmiv, the longest path would be 830 steps long.

What is the length of the longest path that reaches the vault?

Your puzzle input is still edjrjqaa.
"""
from collections import deque
from part1 import moves

def longest_path(code):
    q = deque([('', (0, 0))])
    
    max_path = 0
    while len(q) != 0:
        path, pos = q.popleft()

        if pos != (3,3):
            q.extend([(path + _dir, m) for _dir, m in moves(pos, code, path)])
        else: 
            max_path = max(max_path, len(path))

    return max_path

if __name__ == '__main__':
    assert longest_path('ihgpwlah') == 370
    assert longest_path('kglvqrro') == 492
    assert longest_path('ulqzkmiv') == 830

    print longest_path('edjrjqaa')
