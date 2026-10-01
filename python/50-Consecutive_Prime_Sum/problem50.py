#!/usr/bin/env python3

from libeuler.primes import sieve

LIMIT=1_000


def main():
  print('start!')

  primes = sieve(LIMIT)
  set_of_primes = set(primes)
  consecutive_primes = set()

  test = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 89]

  print(sum(test))

  for i in range(0, len(primes)):
    s = sum(primes[0:i+1])
    if s in set_of_primes:
       consecutive_primes.add(s)

  print(consecutive_primes)

  


  
if __name__ == "__main__":
  main()