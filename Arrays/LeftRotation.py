#!/bin/python3

# Problem Description: https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    length = len(a)
    new_initial_index = d
    new_a = []
    for x in range(0, length):
        index = x + d
        if index > length - 1:
            index = index - length
        new_a.append(a[index])
            
    return new_a
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotLeft(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
