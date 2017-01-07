"""
Advent of code 2016 - Day 8, Part 2

Two-Factor Authentication
===

You come across a door implementing what you can only assume is an
implementation of two-factor authentication after a long game of requirements
telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a
nearby desk). Then, it displays a code on a little screen, and you type that
code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken
everything apart and figured out how it works. Now you just have to work out
what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for
the screen; these instructions are your puzzle input. The screen is 50 pixels
wide and 6 pixels tall, all of which start off, and is capable of three
somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the
screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right
by B pixels. Pixels that would fall off the right end appear at the left end of
the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left
column) down by B pixels. Pixels that would fall off the bottom appear at the
top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel,
causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon
dominate the tiny-code-displaying-screen market. That's what the advertisement
on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display:
after you swipe your card, if the screen did work, how many pixels should be
lit?
"""
import sys, time, curses
import fileinput
from collections import namedtuple

def LED_empty(x, y): return [ [False] * y ] * x
def turn_on(LED, start_x, start_y, len_x=1, len_y=1):
    return [[pix or ((start_x <= x < start_x + len_x) and
                    (start_y <= y < start_y + len_y))
                for (y, pix) in enumerate(row)] for (x, row) in enumerate(LED)]
def LED_rotate_row(LED, x, dist):
    return LED[:x] + [LED[x][-dist:] + LED[x][:-dist]] + LED[x+1:]
def LED_rotate_col(LED, y, dist):
    return zip(*LED_rotate_row(zip(*LED), y, dist))

def LED_to_screen(LED, screen, instruction=''):
    screen.addstr(0, 0, instruction, curses.color_pair(3))
    for row in LED:
        for pixel in row:
            screen.addstr('# ' if pixel else '. ',
                          curses.color_pair(int(pixel) + 1))

        screen.addstr('\n')
    screen.refresh()
    time.sleep(0.02)

def interpret_row(row, LED):
    args = row.split()
    if args[0] == 'rect':
        return turn_on(LED, 0, 0, *reversed(map(int, args[1].split('x'))))
    if args[0] == 'rotate' and args[1] == 'row':
        return LED_rotate_row(LED, int(args[2].split('=')[1]), int(args[4]))
    if args[0] == 'rotate' and args[1] == 'column':
        return LED_rotate_col(LED, int(args[2].split('=')[1]), int(args[4]))

def interpret(instructions, screen=None):
    LED = LED_empty(6, 50)
    if screen is not None: LED_to_screen(LED, screen, '\n\n')
    for line in instructions:
        LED = interpret_row(line, LED)
        if screen is not None: LED_to_screen(LED, screen, line + '\n')
    return LED

def init_screen():
    stdscr = curses.initscr()
    curses.start_color()
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
    return stdscr

if __name__ == '__main__':
    LED = interpret(fileinput.input(), init_screen())
    curses.endwin()
    print sum(map(int, sum(LED, ())))
