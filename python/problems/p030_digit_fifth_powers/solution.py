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

def solve() -> int:
  limit = upper_limit()

  sum = 0
  for i in range(2, limit+1):
    if isFifthSum(i):
      sum += i


  return sum


def main():
    print(solve())


if __name__ == "__main__":
    main()
