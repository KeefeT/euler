#!/usr/bin/env python3

def main():
  print("start!")

  winners = set()

  for denominator in range(99, 10, -1):
    for numerator in range(denominator-1, 10, -1):
      if numerator % 10 == 0 and denominator % 10 == 0:
        continue


      n = str(numerator)
      d = str(denominator)
      dn = {char: n.count(char) for char in n}
      dd = {char: d.count(char) for char in d}
      has_overlap = bool(dn.keys() & dd.keys())

      if has_overlap == False:
        continue

      matching_keys = list(dn.keys() & dd.keys())

      for k in matching_keys:
        copy_n = int(n.replace(k, "", 1))
        copy_d = int(d.replace(k, "", 1))

        if copy_d == 0:
          continue

        if (numerator / denominator) == (int(copy_n) / copy_d):
          winners.add((numerator, denominator))

  print(winners)

  product_n = 1
  product_d = 1
  for winner in winners:
    n, d = winner
    product_n = product_n * n
    product_d = product_d * d

  print(product_n)
  print(product_d)









main()