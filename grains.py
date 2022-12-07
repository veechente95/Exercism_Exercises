# https://exercism.org/tracks/python/exercises/grains
# Calculate the number of grains of wheat on a chessboard given that the number on each square doubles.

def square(number):
    if number >= 1 and number <= 64:
        return 2 ** (number - 1)
    else:
        raise ValueError("square must be between 1 and 64")
    pass


def total():
    return sum([2**i for i in range(64)])
