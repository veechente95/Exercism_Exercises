# Determine if a triangle is equilateral, isosceles, or scalene.
# An equilateral triangle has all three sides the same length.
# An isosceles triangle has at least two sides the same length. 
# (It is sometimes specified as having exactly two sides the same length, but for the purposes of this exercise we'll say at least two.)
# A scalene triangle has all sides of different lengths.
def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b and c:
        return True
    elif a != b or c:
        return False
    else:
        return False

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b or c:
        return True
    elif sides[2] == a or b or c:
        return False


def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a == b or c:
        return True
    elif a != b or c:
        return False


