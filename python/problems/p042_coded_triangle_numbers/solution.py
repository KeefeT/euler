#!/usr/bin/env python3

from pathlib import Path

def getWordValue(name: str):
    name = name.lower()

    val = 0
    for letter in name:
      val += ord(letter) - 96

    return val

def triangle(n: int):
  return (n *(n+1))//2

def isTriangleWord(word: str) -> bool:
  value = getWordValue(word)

  limit = value

  for i in range(limit, 0, -1):
    if value == triangle(i):
      return True

  return False


def solve() -> int:
  with open(Path(__file__).with_name("words.txt"), 'r') as file:
    words = file.readline().replace("\"", "").split(',')

  triangleWords = 0
  for word in words:
    if isTriangleWord(word):
      triangleWords += 1

  return triangleWords


def main():
    print(solve())


if __name__ == "__main__":
    main()
