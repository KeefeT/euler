#!/usr/bin/env python3

LIMIT=28123

def get_divisors(n: int) -> list:
  if n <= 1:
    return []
  divisors = [1]
  for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
      divisors.append(i)
      other = n // i
      if other != i:
        divisors.append(other)
  return divisors

def isAbundantNumber(n: int) -> bool:
  return sum(get_divisors(n)) > n


def solve() -> int:

  l = set()
  a = list()

  for i in range(1, 28123+1):
    l.add(i)
    if isAbundantNumber(i):
      a.append(i)

  for i in range(0, len(a)):
    for j in range(i, len(a)):
      sumation = a[i] + a[j]
      if sumation > LIMIT:
        break
      l.discard(sumation)

  return sum(l)


def main():
    print(solve())


if __name__ == "__main__":
    main()
