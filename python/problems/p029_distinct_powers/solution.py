#!/usr/bin/env python3

LIMIT=100

def solve() -> int:
  unique_powers = set()

  for a in range(2, LIMIT+1):
    for b in range(2, LIMIT+1):
      unique_powers.add(a ** b)

  return len(unique_powers)


def main():
    print(solve())


if __name__ == "__main__":
    main()
