#!/bin/python3

#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/problem?isFullScreen=true

import sys
import logging
import math

DEBUG_LEVEL = logging.DEBUG
logger = logging.getLogger('euler007')
logging.basicConfig(level=DEBUG_LEVEL)


t = int(input().strip())

cache = [2,3,5,7,11,13,17,19,23,29]

for a0 in range(t):

    #need to find nth prime number
    n = int(input().strip())

    logger.debug(f"Finding {n}")

    largest_prime_index = len(cache)
    largest_prime = cache[len(cache)-1]

    if n <= largest_prime_index:
        print(cache[n-1])
    else:
        found_prime = False
        prime_candidate = largest_prime

        while not found_prime:
            prime_candidate += 1

            logger.debug(f"Evaluating {prime_candidate}")

            found_prime = True

            if prime_candidate % 2 == 0:
                break

            #for p in cache:
            #    if prime_candidate % p == 0:
            #        break

            for i in range(2,prime_candidate-1):
                if prime_candidate % i == 0:
                    logger.debug(f"{prime_candidate} is not a prime")
                    found_prime = False
                    break

            if found_prime is True:                
                cache.append(prime_candidate)
                logger.debug(f"{prime_candidate} is the {len(cache)}th prime")

            if len(cache) == n:
                print(prime_candidate)
            else:
                found_prime = False

    #print(n)
