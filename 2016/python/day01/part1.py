"""
Advent of code 2016 - Day 1, Part 1

No Time for a Taxicab
===

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near",
unfortunately, is as close as you can get - the instructions on the Easter
Bunny Recruiting Document the Elves intercepted start here, and nobody had time
to work them out further.

The Document indicates that you should start at the given coordinates (where
you just landed) and face North. Then, follow the provided sequence: either
turn left (L) or right (R) 90 degrees, then walk forward the given number of
blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you
take a moment and work out the destination. Given that you can only walk on the
street grid of the city, how far is the shortest path to the destination?
"""
import fileinput
import operator as op
import re

# Convenience methods.
def block_dist_str(dist, direction):
    return "" if dist == 0 else "{} blocks {}".format(abs(dist), direction)
def neg_if_true(val): return {True: -1, False: 1}[val]

# Vector operations.
def vect_add(vect1, vect2): return map(op.add, vect1, vect2)
def vect_scale(scale, vect): return map(op.mul, [scale]*len(vect), vect)

# Iterate through each comma-separated pair of directions;
# first split the string based on commas (and eat up any additional
# whitespace), then split the direction-changing bit of the instruction,
# and the distance part (which should be an int).
def get_dir_dest_list(description):
    return map(lambda x: (x[0], int(x[1:])), re.split(',\s+', description))

def move(turn, distance, direction, position):
    # Essentially matrix operations, transforming the vector to:
    # R rotates _dir as: ( 1,  0) -> ( 0,  1) -> (-1,  0) -> ( 0, -1)
    # L rotates _dir as: ( 1,  0) -> ( 0, -1) -> (-1,  0) -> ( 0,  1)
    direction = [neg_if_true(turn == 'R') * direction[1],
                 neg_if_true(turn == 'L') * direction[0]]
    # New pos by vector addition of current po and the scaled direction vector
    position = vect_add(position, vect_scale(distance, direction))

    return position, direction

def get_distance_position_string(pos):
    # Remove empty direction entries (e.g., saying 0 blocks east does not make
    # any sense).
    return ", ".join(filter(lambda x: x != "", [
        block_dist_str(pos[0], 'North' if pos[0] >= 0 else 'South'),
        block_dist_str(pos[1], 'East' if pos[1] >= 0 else 'West'),
        "A total of " + block_dist_str(abs(pos[0]) + abs(pos[1]), 'away')]))

def no_taxi_cab(description):
    # Starting on position 0, 0, in a northwards direction.
    _pos, _dir = [0, 0], [1, 0]

    for (turn, distance) in get_dir_dest_list(description):
        _pos, _dir = move(turn, distance, _dir, _pos)

    return get_distance_position_string(_pos)

# Sanity tests given from example input.
assert no_taxi_cab("R2, L3") == \
    "3 blocks North, 2 blocks East, A total of 5 blocks away"
assert no_taxi_cab("R2, R2, R2") == \
    "2 blocks South, A total of 2 blocks away"
assert no_taxi_cab("R5, L5, R5, R3") == \
    "2 blocks North, 10 blocks East, A total of 12 blocks away"

if __name__ == '__main__':
    print no_taxi_cab(reduce(op.add, fileinput.input()))
