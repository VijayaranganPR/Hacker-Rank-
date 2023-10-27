#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    
    # these two are the one I wrote
    # use the function inside the key to decide how to sort.
    for i in sorted(arr, key = lambda x: x[k]):
        print(*i)
