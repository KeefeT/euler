#!/usr/bin/env python3

LIMIT=28123

def get_divisors(n: int) -> list:
  divisors = list()
  for i in range(1, n // 2 + 1):
    if n % i == 0:
      divisors.append(i)

  return divisors

def isAbundantNumber(n: int) -> bool:
  return sum(get_divisors(n)) > n
    

def main():
  print('start!')

  l = set()
  a = list()

  for i in range(1, 28123+1):
    l.add(i)
    if isAbundantNumber(i):
      a.append(i)

  for i in range(0, len(a)):
    print(f'i={i}, len(a)={len(a)}')
    for j in range(i, len(a)):
      sumation = a[i] + a[j]
      l.discard(sumation)

  print(sum(l))


if __name__ == "__main__":
  main()