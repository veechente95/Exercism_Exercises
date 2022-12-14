# Determine if a triangle is equilateral, isosceles, or scalene.
# An equilateral triangle has all three sides the same length.
# An isosceles triangle has at least two sides the same length. 
# (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
# A scalene triangle has all sides of different lengths.

def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == 0 and b == 0 and c == 0:
        return False
    else:
        return (a == b and a == c)


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a == 0 and b == 0 and c == 0) or (a + b < c or a + c < b or b + c < a):
        return False
    else:
        return (a == b or b == c or a == c)


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if (a == 0 and b == 0 and c == 0) or (a + b < c or a + c < b or b + c < a):
        return False
    else:
        return (a != b and b != c and a != c)
