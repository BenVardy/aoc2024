import sys


def read_input() -> str:
    with open(sys.argv[1], "r") as f:
        return f.read()