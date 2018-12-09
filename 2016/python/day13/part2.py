"""
Advent of code 2016 - Day 13, Part 1

A Maze of Twisty Little Cubicles
===
How many locations (distinct x,y coordinates, including your starting location)
can you reach in at most 50 steps?

Your puzzle input is still 1364.
"""
from part1 import Pos, moves, serialize, valid
from collections import deque

def reachable_positions(start, steps, designer):
    q = deque([(0, start)])
    visited = set()

    while len(q) > 0:
        iteration, pos = q.popleft()
        serialized_pos = serialize(pos)

        if serialized_pos in visited: continue
        visited.add(serialized_pos)

        if iteration < steps:
            q.extend([(iteration + 1, m) for m in moves(pos) if valid(m, designer)])

    return visited

if __name__ == '__main__':
    designer = 1364
    print " Able to visit {} positions.".format(
            len(reachable_positions(Pos(1,1), 50, designer)))
