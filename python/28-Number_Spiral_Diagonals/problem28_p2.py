#!/usr/bin/env python3

EDGE_SIZE_OF_SPIRAL=1001

def get_corners_sum(side_length: int):
  if side_length == 1:
    return 1

  square = side_length ** 2
  n = side_length - 1

  sum = 0
  for i in range(0, 4):
    sum += (square - (i * n))


  print(f'sum of {side_length}x{side_length} square corners: {sum}')
  return sum



def main():
  print("start!")

  sum = 0
  for i in range(1, EDGE_SIZE_OF_SPIRAL+1, 2):
    sum += get_corners_sum(i)

  print(f'sum of corners for spiral size n={EDGE_SIZE_OF_SPIRAL} is {sum}')

  






main()