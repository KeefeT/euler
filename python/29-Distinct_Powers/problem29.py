#!/usr/bin/env python3

LIMIT=100

def main():
  print('start!')
  unique_powers = set()

  for a in range(2, LIMIT+1):
    for b in range(2, LIMIT+1):
      unique_powers.add(a ** b)

  print(unique_powers)
  print(len(unique_powers))


if __name__ == "__main__":
  main()