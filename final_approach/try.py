import os
import sys
from collections import defaultdict, Counter


def main():
    file = open("transcript.txt", "r")
    L = list(file.read().splitlines())[-1]


if __name__ == "__main__":
    main()
