#!/usr/bin/env python3

from pathlib import Path

SPAN_LENGTH=4
SPANS = ["up", "down", "left", "right", "up-left", "up-right", "down-left", "down-right"]

def is_out_of_bounds(x: int, y: int, grid: list[list]) -> bool:
  y_len = len(grid)
  x_len = len(grid[0])
  if y >= y_len or y < 0:
    print(f'{y} is out of bounds! (y)')
    return True
  elif x >= x_len or x < 0:
    print(f'{x} is out of bounds! (x)')
    return True
  else:
    return False

def is_span_in_range(x: int, y: int, grid: list[list], span_length: int, direction: str) -> bool:
  if is_out_of_bounds(x, y, grid):
    return False

  span_length = span_length - 1
  y_len = len(grid)
  x_len = len(grid[0])


  match direction:
    case "up":
      if y-span_length < 0:
        return False
    case "down":
      if y+span_length >= y_len:
        return False
    case "left":
      if x-span_length < 0:
        return False
    case "right":
      if x+span_length >= x_len:
        return False
    case "up-left":
      return is_span_in_range(x,y,grid, span_length+1, "up") and is_span_in_range(x,y,grid, span_length+1, "left")
    case "up-right":
      return is_span_in_range(x,y,grid, span_length+1, "up") and is_span_in_range(x,y,grid, span_length+1, "right")
    case "down-left":
      return is_span_in_range(x,y,grid, span_length+1, "down") and is_span_in_range(x,y,grid, span_length+1, "left")
    case "down-right":
      return is_span_in_range(x,y,grid, span_length+1, "down") and is_span_in_range(x,y,grid, span_length+1, "right")
    case _:
      print(f'unknown direction "{direction}"!')
      return False

  return True

def calc_span(x: int, y: int, grid: list[list], span_length: int, direction: str):
  if not is_span_in_range(x, y, grid, span_length, direction):
    print(f'{direction} span is not in range for size {span_length} at ({x},{y})')
    return 0

  product = 1
  y_mod = 0
  x_mod = 0

  if "up" in direction:
    y_mod = -1
  
  if "down" in direction:
    y_mod = 1
  
  if "left" in direction:
    x_mod = -1
  
  if "right" in direction:
    x_mod = 1

  for i in range(0, span_length):
    print(f'{grid[y+(y_mod*i)][x+(x_mod*i)]}', end=' * ')
    product *= grid[y+(y_mod*i)][x+(x_mod*i)]

  print()

  print(f'span of "{direction}" of length {span_length} at ({x},{y}) is {product}')

  return product

def calc_all_spans(x: int, y: int, grid: list[list], span_length: int):
  products = []
  for span in SPANS:
    products.append(calc_span(x, y, grid, span_length, span))

  return products

def main():
  grid = []
  with open(Path(__file__).with_name("grid.txt"), 'r') as file:
    for line in file:
      grid.append(list(map(int, line.split(" "))))

  greatest = 0

  for y in range(0, len(grid)):
    for x in range(0, len(grid[0])):
      products = calc_all_spans(x, y, grid, SPAN_LENGTH)
      for product in products:
        if product > greatest:
          greatest = product

  print(greatest)

main()