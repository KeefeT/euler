#!/usr/bin/env python3

def pow5(n: int) -> int:
  return n ** 5

def upper_limit():
  nine_to_the_fifth = pow5(9)
  n = 1

  while nine_to_the_fifth > n:
    n *= 10

  limit_digits = len(str(n))
  max_limit = nine_to_the_fifth * limit_digits
  print(f"max possible number = {max_limit} (9^5 * {limit_digits})")
  return max_limit

def isFifthSum(n: int) -> bool:
  s = str(n)

  sum = 0
  for c in s:
    sum += pow5(int(c))

  if n == sum:
    return True
  else:
    return False

def main():
  limit = upper_limit()

  sum = 0
  for i in range(2, limit+1):
    if isFifthSum(i):
      print(f'{i} is the sum of its digits each raised to the fifth!')
      sum += i


  print(sum)




main()