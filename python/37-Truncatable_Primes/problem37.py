#!/usr/bin/env python3

PRIMES = {2, 3, 5, 7}

def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []

    # 1. Create a boolean array initialized to True
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime

    # 2. Only loop up to the square root of the limit
    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            # 3. Directly jump to multiples of p and mark them False
            # Start at p*p because smaller multiples are already marked
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    # 4. Extract the indices that are still True
    primes = [i for i, prime in enumerate(is_prime) if prime]
    print(primes)
    return primes

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

  digits_r = [int(c) for c in str(n)]
  digits_l = [int(c) for c in str(n)]

  return truncate(digits_l, 0) and truncate(digits_r, -1)

def main():
  print('start!')
  truncatable_primes = set()
  n = 1000

  while len(truncatable_primes) < 11:
    n = n * 10
    PRIMES.update(sieve(n))
    

    for prime in PRIMES:
      if prime in truncatable_primes:
        continue

      if isTruncatable(prime):
        print(f'new truncatable prime! Pt={prime}')
        truncatable_primes.add(prime)

    

  print()
  print("truncatable primes: ")
  print(truncatable_primes)

  print(f'sum of truncatable primes = {sum(truncatable_primes)}')

if __name__ == "__main__":
  main()