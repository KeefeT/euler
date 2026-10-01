#!/usr/bin/env python3

LIMIT=10_000

def proper_divisors_sum(n: int) -> int:
  sum_of_proper_divisors = 1
  i = 2
  while (i * i) <= n:
    if n % i == 0:
      sum_of_proper_divisors += i
      sum_of_proper_divisors += n // i
    i += 1

  return sum_of_proper_divisors


def main():
  print('start!')
  amicable = set()
  n = 1
  while n <= LIMIT:
    d1 = proper_divisors_sum(n)
    d2 = proper_divisors_sum(d1)
    if d1 == d2:
      n += 1
      continue
    

    if n == d2:
      print(f'{n} and {d1} are amicable!')
      amicable.add(n)
      amicable.add(d1)
      n = d1 + 1
      continue

    n += 1

  print(sum(amicable))



if __name__ == "__main__":
  main()