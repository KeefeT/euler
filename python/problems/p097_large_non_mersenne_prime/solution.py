#!/usr/bin/env python3

BASE=2
EXP=7830457
MULT=28433

def solve() -> int:
  n = (pow(BASE, EXP, 10 ** 10) * MULT + 1) % (10 ** 10)
  res = 0

  for i in range(0, 10):
    place = (10 ** i)
    res += (n % 10) * place
    n //= 10

  return res


def main():
    print(solve())


if __name__ == "__main__":
    main()
