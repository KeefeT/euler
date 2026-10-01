#!/usr/bin/env python3

from collections import defaultdict

def triangle(n: int) -> int:
  t = (n*(n+1))//2
  print(f"[tri] tri of {n} is {t}")
  return t

def pentagonal(n: int) -> int:
  p = (n*(3*n-1))//2
  print(f"[pent] pent of {n} is {p}")
  return p

def hexagonal(n: int) -> int:
  h = (n*(2*n-1))
  print(f"[hex] hex of {n} is {h}")
  return h

def main():
  n = 285
  print("start!")
  found = False

  triangles = defaultdict(int)
  pentagonals = defaultdict(int)
  hexagonals = defaultdict(int)

  test = 55385

  print(triangle(test)) # <-------
  print(hexagonal(test))
  print(pentagonal(test))

  found = True


  while not found:
    n += 1
    # print(f'now trying n={n}')
    t = triangles[n]
    if t == 0:
      triangles[n] = triangle(n)
      t = triangles[n]

    for i in range(n, n//2, -1):
      p = pentagonals[i]
      if p == 0:
        pentagonals[i] = pentagonal(i)
        p = pentagonals[i]
      if t == p:
        for j in range(n, n//2, -1):
          h = hexagonals[j]
          if h == 0:
            hexagonals[j] = hexagonal(j)
            h = hexagonals[j]
          if t == h:
            found = True
            break


  print(n)



main()