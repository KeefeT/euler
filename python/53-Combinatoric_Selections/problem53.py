#!/usr/bin/env python3


def combinations(n_f, n, r):
  return (n_f) // (factorial(r) * factorial(n-r))

def factorial(n: int):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n-1)

def main():
  print('start!')

  winners = list()
  for n in range(2, 101):
    n_f = factorial(n)
    for r in range(1, n):
      combos = combinations(n_f, n, r)
      if combos > 1_000_000:
        winners.append(combos)


  print(winners)
  print(len(winners))


  
if __name__ == "__main__":
  main()