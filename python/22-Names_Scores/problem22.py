#!/usr/bin/env python3

from pathlib import Path

def bubbleSort(arr: list):
  length = len(arr)

  for i in range(length):
    for j in range(0, length-i-1):
        if arr[j].lower() > arr[j+1].lower():
          arr[j], arr[j+1] = arr[j+1], arr[j]

  return arr

def getNameValue(name: str):
    name = name.lower()

    print(f'name is {name}')
    val = 0
    for letter in name:
      print(f'{letter} is {ord(letter)}')
      val += ord(letter) - 96

    return val






def main():
  print("hello")

  with open(Path(__file__).with_name("names.txt"), 'r') as file:
    names = file.readline().replace("\"", "").split(',')
    sorted = bubbleSort(names)

    i = 1
    total = 0
    for name in sorted:
      total += getNameValue(name) * i
      i += 1

    print(total)
        




main()