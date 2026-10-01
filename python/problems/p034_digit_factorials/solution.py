#!/usr/bin/env python3


def factorial(n: int) -> int:
  if n == 0 or n == 1:
    return 1
  return n * factorial(n - 1)

def find_upper_limit():
  nine_factorial = factorial(9)
  digits = 1

  while (nine_factorial > digits):
    digits *= 10

  return len(str(digits)) * nine_factorial

def solve() -> int:
  limit = find_upper_limit() + 1
  factorials = []
  for i in range(0,10):
    factorials.append(factorial(i))


  total = 0
  for i in range(3, limit):
    sum = 0
    number = str(i)
    for letter in number:
      sum += factorials[int(letter)]
    if sum == i:
      total += i

  return total


def main():
    print(solve())


if __name__ == "__main__":
    main()
