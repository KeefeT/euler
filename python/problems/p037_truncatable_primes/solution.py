#!/usr/bin/env python3

from libeuler.primes import sieve

PRIMES = {2, 3, 5, 7}


def truncate(l: list, pop_idx: int):

  if len(l) <= 1:
    return False

  while len(l) > 1:
    l.pop(pop_idx)
    res = 0
    for digit in l:
      res = res * 10 + digit

    if res not in PRIMES or res == 0:
      return False

  return True

def isTruncatable(n: int) -> bool:
  if n < 10 or n not in PRIMES:
    return False

  digits_r = [int(c) for c in str(n)]
  digits_l = [int(c) for c in str(n)]

  return truncate(digits_l, 0) and truncate(digits_r, -1)

def solve() -> int:
  global PRIMES
  PRIMES = {2, 3, 5, 7}
  truncatable_primes = set()
  n = 1000

  while len(truncatable_primes) < 11:
    n = n * 10
    PRIMES.update(sieve(n))


    for prime in PRIMES:
      if prime in truncatable_primes:
        continue

      if isTruncatable(prime):
        truncatable_primes.add(prime)




  return sum(truncatable_primes)


def main():
    print(solve())


if __name__ == "__main__":
    main()
