"""
Advent of code 2016 - Day 19, Part 2

An Elephant Named Joseph
===
Realizing the folly of their present-exchange rules, the Elves agree to
instead steal presents from the Elf directly across the circle. If two Elves
are across the circle, the one on the left (from the perspective of the
stealer) is stolen from. The other rules remain unchanged: Elves with no
presents are removed from the circle entirely, and the other elves move in
slightly to keep the circle evenly spaced.

For example, with five Elves (again numbered 1 to 5):

    The Elves sit in a circle; Elf 1 goes first:

      1
    5   2
     4 3

    Elves 3 and 4 are across the circle; Elf 3's present is stolen, being the
    one to the left. Elf 3 leaves the circle, and the rest of the Elves move
    in:

      1           1
    5   2  -->  5   2
     4 -          4

    Elf 2 steals from the Elf directly across the circle, Elf 5:

      1         1 
    -   2  -->     2
      4         4 

    Next is Elf 4 who, choosing between Elves 1 and 2, steals from Elf 1:

     -          2  
        2  -->
     4          4

    Finally, Elf 2 steals from Elf 4:

     2
        -->  2  
     -

So, with five Elves, the Elf that sits starting in position 2 gets all the
presents.

With the number of Elves given in your puzzle input, which Elf now gets all
the presents?

Your puzzle input is still 3004953.
"""

def josephus(t):
    """ Specialized Josephus function

    This is special in the sense that it does not have a fixed k (like in
    part 1 where k was 2). This iteratively computes the solution for each n
    up until the desired amount t, with a variable k defined as floor(n/2),
    meaning the opposite of the circle.

    If the previous answer exceeds k, then this is compensated for by adding
    1 to the current answer, as k is already eliminated.
    """
    return reduce(lambda j, n: (j + int(j >= n//2)) % n+1, xrange(2, t+1), 1)

if __name__ == '__main__':
    assert josephus(5) == 2
    print josephus(3004953)

