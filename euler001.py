#!/bin/python3

import sys, logging

t = int(input().strip())

cum_sum_cache = dict()

for a0 in range(t):
    final_sum = 0

    n = int(input().strip())

    nearest_three_factor = int((n-1) / 3.0)
    three_multiple = nearest_three_factor * (nearest_three_factor / 2 + 0.5)
    final_sum += three_multiple * 3

    nearest_five_factor = int((n-1) / 5.0)
    five_multiple = nearest_five_factor * (nearest_five_factor / 2 + 0.5)
    final_sum += five_multiple * 5

    nearest_fifteen_factor = int((n-1) / 15.0)
    fifteen_multiple = nearest_fifteen_factor * (nearest_fifteen_factor / 2 + 0.5)
    final_sum -= fifteen_multiple * 15

    #this works but is slow
    #final_sum = 0

    #for x in range(n):
    #    if x % 5 == 0 or x % 3 == 0:
    #        final_sum += x
    print(int(final_sum))
