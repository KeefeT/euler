#!/usr/bin/env python3


BASES = [2, 10]

def convert_to_binary(n: int):

  num = ""

  while n > 0:
    r = n % 2
    num += str(r)
    n = n // 2

  num = int(num[::-1])

  return num

def is_palindrome(n: int, base: int):
  if base == 2:
    n = convert_to_binary(n)

  rev = int(str(n)[::-1])

  # if n != rev:
  #   print(f'{n} is not a palindrome in b{base}')
  # else:
  #   print(f'{n} is a palindrome in b{base}')

  return n == rev
  



def main():
  print("start!")

  n = 1
  sum = 0
  while n < 1_000_000:
    total_match = True
    for base in BASES:
      total_match = is_palindrome(n, base) and total_match

    if total_match:
      print(f"{n} is palendromic for these bases: {BASES}")
      sum += n

    n += 1

  print(sum)




main()