from enum import Enum


class Color(Enum):
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)

    COLORS = [BLUE, RED, YELLOW, GREEN]


class Number(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

    NUMBERS = [1, 2, 3, 4]


class Shape(Enum):
    # TODO: replace int values with coordinates to draw shapes
    SQUARE = 1
    CIRCLE = 2
    TRIANGLE = 3
    STAR = 4

    SHAPES = [SQUARE, CIRCLE, TRIANGLE, STAR]