#!/usr/bin/env python3

BASE=2
EXP=7830457
MULT=28433

def main():
  n = ((BASE ** EXP) * MULT) + 1
  res = 0

  for i in range(0, 10):
    place = (10 ** i)
    res += (n % 10) * place
    n //= 10

  print(len(str(res)))
  print(res)
  
if __name__ == "__main__":
  main()