"""
Advent of code 2016 - Day 2, Part 1

Bathroom security
===

You arrive at Easter Bunny Headquarters under cover of darkness. However, you
left in such a rush that you forgot to use the bathroom! Fancy office buildings
like this one usually have keypad locks on their bathrooms, so you search the
front desk for the code.

"In order to improve security," the document you find says, "bathroom codes
will no longer be written down. Instead, please memorize and follow the
procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by
starting on the previous button and moving to adjacent buttons on the keypad: U
moves up, D moves down, L moves left, and R moves right. Each line of
instructions corresponds to one button, starting at the previous button (or,
for the first line, the "5" button); press whatever button you're on at the end
of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk
to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and
stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then
down three times (stopping at "9" after two moves and ignoring the third),
ending up with 9. Continuing from "9", you move left, up, right, down, and left,
ending with 8. Finally, you move up four times (stopping at "2"), then down
once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front
desk. What is the bathroom code?
"""
import fileinput
import operator as op

def within(pos, keypad):
    return (pos[0] >= 0 and pos[0] < len(keypad)) and \
           (pos[1] >= 0 and pos[1] < len(keypad[pos[0]])) and \
           keypad[pos[0]][pos[1]] is not None

# Vector operations.
def vect_add(vect1, vect2): return map(op.add, vect1, vect2)

default_keypad = [[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]]

def bathroom_security(keypad, description):
    # Starting in the middle, at 5, by finding the index of 5
    pos = next([i, s.index(5)] for i, s in enumerate(keypad) if 5 in s)
    direction_map = {
        'L': [ 0, -1],
        'R': [ 0,  1],
        'D': [ 1,  0],
        'U': [-1,  0]}

    code = ""
    for line in description:
        for direction in line.strip():
            new_pos = vect_add(pos, direction_map[direction])
            if within(new_pos, keypad):
                pos = new_pos
        code = code + str(keypad[pos[0]][pos[1]])

    return code

# Sanity check
assert bathroom_security(default_keypad, ["ULL", "RRDDD", "LURDL", "UUUUD"]) \
    == "1985"

if __name__ == '__main__':
    print bathroom_security(default_keypad, fileinput.input())
