#!/usr/bin/env python3

from libeuler.primes import sieve

LIMIT=(10 ** 7)


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