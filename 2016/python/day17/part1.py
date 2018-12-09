"""
Advent of code 2016 - Day 17, Part 1

Two Steps Forward
===

You're trying to access a secure vault protected by a 4x4 grid of small rooms
connected by doors. You start in the top-left room (marked S), and you can
access the vault (marked V) once you reach the bottom-right room:

#########
#S| | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | | #
#-#-#-#-#
# | | |  
####### V

Fixed walls are marked with #, and doors are marked with - or |.

The doors in your current room are either open or closed (and locked) based
on the hexadecimal MD5 hash of a passcode (your puzzle input) followed by a
sequence of uppercase characters representing the path you have taken so far
(U for up, D for down, L for left, and R for right).

Only the first four characters of the hash are used; they represent,
respectively, the doors up, down, left, and right from your current position.
Any b, c, d, e, or f means that the corresponding door is open; any other
character (any number or a) means that the corresponding door is closed and
locked.

To access the vault, all you need to do is reach the bottom-right room;
reaching this room opens the vault and all doors in the maze.

For example, suppose the passcode is hijkl. Initially, you have taken no steps,
and so your path is empty: you simply find the MD5 hash of hijkl alone. The
first four characters of this hash are ced9, which indicate that up is open
(c), down is open (e), left is open (d), and right is closed and locked (9).
Because you start in the top-left corner, there are no "up" or "left" doors
to be open, so your only choice is down.

Next, having gone only one step (down, or D), you find the hash of hijklD.
This produces f2bc, which indicates that you can go back up, left (but that's
a wall), or right. Going right means hashing hijklDR to get 5745 - all doors
closed and locked. However, going up instead is worthwhile: even though it
returns you to the room you started in, your path would then be DU, opening a
different set of doors.

After going DU (and then hashing hijklDU to get 528e), only the right door is
open; after going DUR, all doors lock. (Fortunately, your actual passcode is
not hijkl).

Passcodes actually used by Easter Bunny Vault Security do allow access to the
vault if you know the right path. For example:

    If your passcode were ihgpwlah, the shortest path would be DDRRRD.
    With kglvqrro, the shortest path would be DDUDRLRRUDRD.
    With ulqzkmiv, the shortest would be DRURDRUDDLLDLUURRDULRLDUUDDDRR.

Given your vault's passcode, what is the shortest path (the actual path, not
just the length) to reach the vault?

Your puzzle input is edjrjqaa.
"""
from collections import deque
import md5

DIRS = [('U', (0, -1)), ('D', (0, 1)), ('L', (-1, 0)), ('R', (1, 0))]

def unlocked(seed):
    return (int(x, 16) > 10 for x in  md5.new(seed).hexdigest())

def on_field(pair):
    return all([0 <= x < 4 for x in pair[1]])

def moves(pos, passcode, path):
    is_open = unlocked(passcode + path)
    return filter(on_field,
        [(c, tuple(map(sum, zip(pos, d)))) for c, d in DIRS if next(is_open)])

def shortest_path(passcode):
    q = deque([('', (0, 0))])

    while len(q) != 0:
        path, pos = q.popleft()

        if pos == (3, 3):
            return path

        q.extend([(path + _dir, m) for _dir, m in moves(pos, passcode, path)])

if __name__ == '__main__':
    assert shortest_path('ihgpwlah') == 'DDRRRD'
    assert shortest_path('kglvqrro') == 'DDUDRLRRUDRD'
    assert shortest_path('ulqzkmiv') == 'DRURDRUDDLLDLUURRDULRLDUUDDDRR'

    print shortest_path('edjrjqaa')
