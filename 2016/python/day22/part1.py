"""
Advent of code 2016 - Day 22, Part 1

Grid Computing
===

You gain access to a massive storage cluster arranged in a grid; each storage
node is only connected to the four nodes directly adjacent to it (three if the
node is on an edge, two if it's in a corner).

You can directly access data only on node /dev/grid/node-x0-y0, but you can
perform some limited actions on the other nodes:

 - You can get the disk usage of all nodes (via df). The result of doing this
   is in your puzzle input.
 - You can instruct a node to move (not copy) all of its data to an adjacent
   node (if the destination node has enough space to receive the data). The
   sending node is left empty after this operation.

Nodes are named by their position: the node named node-x10-y10 is adjacent to
nodes node-x9-y10, node-x11-y10, node-x10-y9, and node-x10-y11.

Before you begin, you need to understand the arrangement of data on these
nodes. Even though you can only move data between directly connected nodes,
you're going to need to rearrange a lot of the data to get access to the data
you need. Therefore, you need to work out how you might be able to shift data
around.

To do this, you'd like to count the number of viable pairs of nodes. A viable
pair is any two nodes (A,B), regardless of whether they are directly
connected, such that:

 - Node A is not empty (its Used is not zero).
 - Nodes A and B are not the same node.
 - The data on node A (its Used) would fit on node B (its Avail).

How many viable pairs of nodes are there?
"""
import fileinput, re
from collections import namedtuple
from itertools import permutations

Node = namedtuple('Node', ['pos', 'size', 'used', 'avail', 'percent'])

def to_node(pos, *args):
    return Node(tuple(map(int, re.findall(r'\d+', pos))), 
                *map(int, (x[:-1] for x in args)))

def nodes(data):
    return (to_node(*re.split(r' +', l)) for l in data if l.startswith('/dev'))

def viable_nodes(data):
    return ((a, b) for a, b, in permutations(nodes(data), 2) 
                if a.used > 0 and a.used <= b.avail)

if __name__ == '__main__':
    print sum(1 for i in viable_nodes(x.strip() for x in fileinput.input()))

