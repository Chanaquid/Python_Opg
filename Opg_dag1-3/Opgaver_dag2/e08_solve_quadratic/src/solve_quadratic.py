#!/usr/bin/env python3

import math

def solve_quadratic(a, b, c):
    d = math.sqrt(b**2 - 4*a*c)
    
    calc_1 = (-b + d) / (2*a)
    calc_2 = (-b - d) / (2*a)
    return (calc_1, calc_2)


def main():
    print(solve_quadratic(1, -3, 2))
    print(solve_quadratic(1, 2, 1))

if __name__ == "__main__":
    main()
