#!/bin/python3

#https://www.hackerrank.com/contests/projecteuler/challenges/euler006/problem?isFullScreen=true

import sys
import logging

DEBUG_LEVEL = logging.DEBUG
logger = logging.getLogger('euler006')
logging.basicConfig(level=DEBUG_LEVEL)


t = int(input().strip())

cache = []

for a0 in range(t):
    n = int(input().strip())

    if len(cache) == 0:
        sums = sum_of_squares = lower_range = 0

    elif len(cache) < n+1:
        lower_range = len(cache)
        sums, sum_of_squares = cache[len(cache)-1]

    for i in range(lower_range,n+1):
        sums += i
        sum_of_squares += i*i
        cache.append((sums, sum_of_squares))
    
    print(sums ** 2 - sum_of_squares)
