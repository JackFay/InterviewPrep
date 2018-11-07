#!/bin/python3

# Problem Description: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    swaps = 0
    for i in range(len(q) - 1, -1, -1):
        if q[i] - (i + 1) > 2:
            return print("Too chaotic")
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                swaps = swaps + 1
                
    return print(swaps)
            
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)