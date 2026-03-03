#!/usr/bin/env python3

import sys


def main():
    for line in sys.stdin:
        line = line.strip()
        if line:
            print("no, I'm sure you can do it yourself")


if __name__ == "__main__":
    main()
