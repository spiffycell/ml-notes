#!/usr/bin/python

import sys
from math import log

def entropy(x):
    print(-sum([i * log(i, 2) for i in x]))


if __name__ == "__main__":
    p = [float(sys.argv[1]), float(sys.argv[2])]
    entropy(p)
