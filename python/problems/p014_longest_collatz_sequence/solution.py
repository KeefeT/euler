#!/usr/bin/env python3

LIMIT=1_000_000


def collatz(n: int) -> int:
  steps = 1
  while n != 1:
    steps += 1
    if n % 2 == 0:
      n = n // 2
    else:
      n = (3*n) + 1
  return steps



def solve() -> int:
  max = 0
  max_i = 0

  for i in range(1, LIMIT+1):
    c = collatz(i)
    if c > max:
      max = c
      max_i = i

  return max_i


def main():
    print(solve())


if __name__ == "__main__":
    main()
