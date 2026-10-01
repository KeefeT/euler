#!/usr/bin/env python3

from collections import defaultdict

def map_digits(n: int):
  digits = defaultdict(int)
  s = str(n)

  for c in s:
    digits[c] += 1

  return dict(digits)

def solve() -> int:
  n = 1
  sameDigits = False
  while not sameDigits:
    n_digits = map_digits(n)
    skip = False
    for i in range(2,7):
      if n_digits != map_digits(i*n):
        skip = True
        break

    if skip:
      n += 1
      continue
    else:
      break


  return n


def main():
    print(solve())


if __name__ == "__main__":
    main()
