"""
This module provides functions to calculate the hypothenuse of a triangle
and the area of a triangle.
"""
__author__ = "Chanakya Joshi"
__version__ = "1.0.0"

def hypothenuse(a, b):
    """
    Calculate the length of the hypothenuse of a right-angled triangle.
    """
    return (a**2 + b**2)**0.5

def area(a, b):
    """
    Calculate the area of a triangle.
    """
    return 0.5 * a * b