#!/usr/bin/python

import sys

def gini_index(x):
    print(1 - sum([i**2 for i in x]))

if __name__ == "__main__":
    p = [float(sys.argv[1]), float(sys.argv[2])]    
    gini_index(p)
