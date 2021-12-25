#!/bin/python3

import sys
import logging
from math import sqrt

OPS = 0
DEBUG_LEVEL = logging.INFO
COMMON_PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
logger = logging.getLogger('euler003')
logging.basicConfig(level=DEBUG_LEVEL)
#logger.setLevel(DEBUG_LEVEL)
#logger.addHandler(logging.StreamHandler())

def get_smallest_factor(n):
    global OPS

    #prime_smallest_factor = False
    #for x in COMMON_PRIMES:
    #    OPS += 1
    #    if n % x == 0:
    #        prime_smallest_factor = True
    #        logger.debug("Operation {}: {} % {} == 0".format(OPS, n,x))
    #        return x

    for x in range(2,int(sqrt(n))+1):
        OPS += 1
        logger.debug("Operation {}: Seeing if prime candidate {} has factor {}".format(OPS,n,x))
        if n % x == 0:
            return x
    return None


def evaluate(n):
    logger.debug("Evaluating {}".format(n))
    global OPS
    largest_prime = None

    x = n
    while x > 0:
        OPS += 1
        logger.debug("Operation {}: Seeing if {} % {} == 0 and get_smallest_factor({})"
            .format(OPS, n,x,x))

        factor = get_smallest_factor(x)
        if factor is None:
            logger.debug("Operation {}: {} is prime".format(OPS, x))
            return x
            #largest_prime = x
            #if n % x == 0:
            #    largest_prime = x    
        else:
            logger.debug("Operation {}: {} has factor {}. Subdividing...".format(OPS, x,factor))
            x = (x // factor)

    return largest_prime

t = int(input().strip())

for a0 in range(t):
    n = int(input().strip())
    print(evaluate(n))
    logger.info("Evaluated in {} operations".format(OPS))
    OPS = 0


