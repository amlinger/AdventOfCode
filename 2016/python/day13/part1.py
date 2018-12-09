"""
Advent of code 2016 - Day 13, Part 1

A Maze of Twisty Little Cubicles
===

You arrive at the first floor of this new building to discover a much less 
welcoming environment than the shiny atrium of the last one. Instead, you are
in a maze of twisty little cubicles, all alike.

Every location in this area is addressed by a pair of non-negative integers
(x,y). Each such coordinate is either a wall or an open space. You can't move
diagonally. The cube maze starts at 0,0 and seems to extend infinitely toward
positive x and y; negative values are invalid, as they represent a location
outside the building. You are in a small waiting area at 1,1.

While it seems chaotic, a nearby morale-boosting poster explains, the layout is
actually quite logical. You can determine whether a given x,y coordinate will
be a wall or an open space using a simple system:

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
    If the number of bits that are 1 is even, it's an open space.
    If the number of bits that are 1 is odd, it's a wall.

For example, if the office designer's favorite number were 10, drawing walls as
# and open spaces as ., the corner of the building containing 0,0 would look
like this:

  0123456789
0 .#.####.##
1 ..#..#...#
2 #....##...
3 ###.#.###.
4 .##..#..#.
5 ..##....#.
6 #...##.###

Now, suppose you wanted to reach 7,4. The shortest route you could take is
marked as O:

  0123456789
0 .#.####.##
1 .O#..#...#
2 #OOO.##...
3 ###O#.###.
4 .##OO#OO#.
5 ..##OOO.#.
6 #...##.###

Thus, reaching 7,4 would take a minimum of 11 steps (starting from your current
location, 1,1).

What is the fewest number of steps required for you to reach 31,39?

Your puzzle input is 1364.
"""

from collections import namedtuple, deque

Pos = namedtuple('Pos', ['x', 'y'])

def is_wall(x, y, designer):
    return bool(bin(x*x + 3*x + 2*x*y + y + y*y + designer)[2:].count('1') % 2)

def moves(pos):
    return [Pos(pos.x+1,pos.y), Pos(pos.x, pos.y+1),
            Pos(pos.x-1,pos.y), Pos(pos.x, pos.y-1)]

def serialize(pos):
    return 10000*pos.x + pos.y

def valid(pos, designer):
    return pos.x >= 0 and pos.y >= 0 and not is_wall(pos.x, pos.y, designer)

def find(start, target, designer):
    target_position = serialize(target)
    q = deque([([], start)])
    visited = set()
    while True:
        iteration, pos = q.popleft()
        serialized_pos = serialize(pos)

        if serialized_pos in visited: continue
        visited.add(serialized_pos)

        if serialize(pos) == target_position:
            return iteration + [pos]

        q.extend([(iteration+[pos], m) for m in moves(pos) if valid(m, designer)])

if __name__ == '__main__':
    designer = 1364
    
    path = [serialize(p) for p in find(Pos(1,1), Pos(31,39), designer)]
    def _char(pos):
        return "0" if serialize(pos) in path else (
                '#' if is_wall(pos.x, pos.y, designer) else '.')
    
    print "Solved in {} iterations.".format(len(path)-1)
    #print "  " + "".join([str(i) for i in range(0,10)])
    #for y in range(0, 7):
    #    print "{} {}".format(
    #            y, "".join(_char(Pos(x, y)) for x in range(0, 10)))
