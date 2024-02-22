#!/usr/bin/env python3

def interleave(*lists):
    return [elem for sublist in zip(*lists) for elem in sublist]

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
