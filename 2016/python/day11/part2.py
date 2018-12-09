"""
Advent of code 2016 - Day 11, Part 1

Radioisotope Thermoelectric Generators
===

You step into the cleanroom separating the lobby from the isolated area and
put on the hazmat suit.

Upon entering the isolated containment area, however, you notice some extra
parts on the first floor that weren't listed on the record outside:

    An elerium generator.
    An elerium-compatible microchip.
    A dilithium generator.
    A dilithium-compatible microchip.

These work just like the other generators and microchips. You'll have to get
them up to assembly as well.

What is the minimum number of steps required to bring all of the objects,
including these four new ones, to the fourth floor?
"""
import fileinput
from part1 import solve

if __name__ == '__main__':
    description = [x.strip() for x in fileinput.input()]
    # Add the missing information to the description
    description[0] += (
            'an elerium generator, ' +
            'an elerium-compatible microchip, ' +
            'a dilithium generator, ' +
            'and a dilithium-compatible microchip.')
    solve(description)
