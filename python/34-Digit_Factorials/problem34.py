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

def main():
  limit = find_upper_limit() + 1
  factorials = []
  for i in range(0,10):
    factorials.append(factorial(i))

  print(f'array of factorials: {factorials}')
  print(f'upper_limit={limit}')

  total = 0
  for i in range(3, limit):
    sum = 0
    number = str(i)
    for letter in number:
      sum += factorials[int(letter)]
    if sum == i:
      total += i
      print(f'{i} is a curious number!')

  print(total)





main()