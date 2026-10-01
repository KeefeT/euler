#!/usr/bin/env python3

LIMIT = 1000

def leg_a(p, x):
  return p - (x // 2)

def leg_b(p, x):
  return p - ((p ** 2) // x)

def leg_c(a, b, p):
  return p - a - b


def main():
  print("start!")

  triangles = {}

  for p in range(1, LIMIT+1):
    psq = p ** 2
    mini = int((2 ** 0.5) * p)
    maxi = 2 * p

    triangles.setdefault(p, [])

    print(f'starting search for p={p} in range({mini},{maxi})')

    for x in range(mini, maxi):
      if psq % x == 0:
        a = leg_a(p, x)
        b = leg_b(p, x)
        c = leg_c(a, b, p)

        print(f'triangle found for p={p} with sides [{a},{b},{c}]')

        triangles[p].append((a, b, c))

    
    best_p, longest_list = max(triangles.items(), key=lambda item: len(item[1]), default=(None, []))

    print(best_p)
    print(longest_list)




main()