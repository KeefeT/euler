#!/usr/bin/env python3

LIMIT=(10 ** 7)

def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

PRIMES=set(sieve(LIMIT))

def get_number_of_digits(n: int) -> int:
  digits = 1

  while n > 10:
    digits += 1
    n //= 10

  return digits

def rotate_number(n: int, digits: int) -> int:
  ones = n % 10
  n //= 10
  new = n + (ones * (10 ** (digits-1)))
  return new
   
def isCircular(n: int) -> bool:
  digits = get_number_of_digits(n)
  rotations = digits - 1
  
  for i in range(0, rotations):
    n = rotate_number(n, digits)
    if n not in PRIMES:
      return False


  return True
  
def main():
  print('start!')
  circular_primes = set()

  for p in PRIMES:
    if isCircular(p):
       circular_primes.add(p)

  print(len(circular_primes))


if __name__ == "__main__":
  main()