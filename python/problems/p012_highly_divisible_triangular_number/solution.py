#!/usr/bin/env python3

LIMIT=1_000_000

DIVISORS={}

def get_divisors(n: int) -> list:
  divisors = list()
  for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)


      other = n // i
      if other != i:
        divisors.append(other)

  return divisors

def triangle(n: int) -> int:
  res = n

  while n != 0:
    n = n - 1
    res = res + n

  return res


def solve() -> int:

  n = 1
  rolling = 2
  while len(get_divisors(n)) <= 500:
    n += rolling
    rolling += 1

  return n


def main():
    print(solve())


if __name__ == "__main__":
    main()
