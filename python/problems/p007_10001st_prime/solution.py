###
#
# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#
###

import math

from libeuler.primes import sieve

# sieve moment?
def solve() -> int:

    n = 10001 #th prime
    # https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime
    upper_bound = int(n * (math.log(n) + math.log(math.log(n))))

    l = sieve(upper_bound)

    return l[10000]


def main():
    print(solve())


if __name__ == "__main__":
    main()
