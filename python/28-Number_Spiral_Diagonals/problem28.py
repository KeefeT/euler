#!/usr/bin/env python3

EDGE_SIZE_OF_SPIRAL=5

# 5x5 -> 5 -> 25
# 3x3 -> 3 -> 9
# 1001x1001 -> 1001 -> 1002001
def square_size(n: int) -> int:
  return n**2

def print_grid(grid: list[list]):
  print()
  for y in range(0, EDGE_SIZE_OF_SPIRAL):
    for x in range(0, EDGE_SIZE_OF_SPIRAL):
      print(grid[y][x], end=" ")
    print()
  print()

def print_direction(direction):
  match direction:
    case (0, 1):
      print("⬇️")
    case (0, -1):
      print("⬆️")
    case (1, 0):
      print("➡️")
    case (-1, 0):
      print("⬅️")
    case _:
      print(f"moving unknown direction: {direction}")


def move(x, y, direction):

  print_direction(direction)

  dx, dy = direction

  x = x+dx
  y = y+dy

  return (x, y)

def rotate(direction):
  dx, dy = direction

  x = int()
  y = int()

  if dx == 1 or dx == -1:
    x = 0
  else:
    if dy == -1:
      x = -1
    elif dy == 1:
      x = 1

  if dy == 1 or dy == -1:
    y = 0
  else:
    if dx == -1:
      y = -1
    elif dx == 1:
      y = 1

  new_direction = (x, y)

  print(f'old direction={direction}, new direction={new_direction}')
  return new_direction

def main():
  print("start!")

  size_of_spiral = square_size(EDGE_SIZE_OF_SPIRAL)

  print(f'total of {size_of_spiral} elements in spiral')

  grid = [[0] * EDGE_SIZE_OF_SPIRAL for _ in range(EDGE_SIZE_OF_SPIRAL)]
  x = EDGE_SIZE_OF_SPIRAL//2
  y = EDGE_SIZE_OF_SPIRAL//2
  direction = (1, 0)
  n = 1
  square = 1
  side_length = 1
  steps = 0
  square_walk = square_size(square)
  force_rotate = False

  print_grid(grid)

  while n <= size_of_spiral:
    grid[y][x] = n
    x, y = move(x, y, direction)
    steps += 1

    if steps == side_length:
      force_rotate = True

    if force_rotate:
      direction = rotate(direction)
      steps = 0
      force_rotate = False

    if n == square_walk:
      # finished drawing a square, now up one
      print(f'finished drawing a square of size {square}!')
      side_length = square
      square += 2
      square_walk = square_size(square)
      direction = rotate(direction)
      steps = 0
    
    n += 1

    print_grid(grid)

    


  






main()