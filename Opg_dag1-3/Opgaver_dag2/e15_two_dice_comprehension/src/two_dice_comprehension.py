#!/usr/bin/env python3

def main():
    for pair in [(i, j) for i in range(1, 7) for j in range(1, 7) if(i+j == 5)]:
        print(pair)

if __name__ == "__main__":
    main()
