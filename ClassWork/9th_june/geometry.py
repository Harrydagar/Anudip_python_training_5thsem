# geometry.py
# Module to calculate area and perimeter of 2D shapes

import math

# ---------------- CIRCLE ----------------
def circle_area(r):
    return math.pi * r * r

def circle_perimeter(r):
    return 2 * math.pi * r


# ---------------- RECTANGLE ----------------
def rectangle_area(l, b):
    return l * b

def rectangle_perimeter(l, b):
    return 2 * (l + b)


# ---------------- SQUARE ----------------
def square_area(s):
    return s * s

def square_perimeter(s):
    return 4 * s


# ---------------- TRIANGLE ----------------
def triangle_area(b, h):
    return 0.5 * b * h

def triangle_perimeter(a, b, c):
    return a + b + c