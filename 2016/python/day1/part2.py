"""
Advent of code 2016 - Day 1, Part 2

No Time for a Taxicab
===

Then, you notice the instructions continue on the back of the Recruiting
Document. Easter Bunny HQ is actually at the first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you
visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""
import fileinput
import operator as op
from part1 import (
    move,
    vect_add,
    get_dir_dest_list,
    get_distance_position_string,
)

def no_taxi_cab_twice(description):
    # Starting on position 0, 0, in a northwards direction.
    _pos, _dir = [0, 0], [1, 0]

    # Count visits hej
    visits = [_pos]

    for (turn, distance) in get_dir_dest_list(description):
        # Move the initial turn in one direction, and add that to the list of
        # visits. We also need to check that we have not been here before.
        _pos, _dir = move(turn, 1, _dir, _pos)
        if _pos in visits:
            return get_distance_position_string(_pos)
        visits.append(_pos)

        # Continue in the same direction for the rest of the blocks we need to
        # move. Thisi is to ensure that
        for _ in range(distance - 1):
            _pos = vect_add(_pos, _dir)
            if _pos in visits:
                return get_distance_position_string(_pos)
            visits.append(_pos)

# Sanity tests given from example input.
assert no_taxi_cab_twice("R8, R4, R4, R8") == \
    "4 blocks East, A total of 4 blocks away"

if __name__ == '__main__':
    print no_taxi_cab_twice(reduce(op.add, fileinput.input()))
