EDGE_SIZE_OF_SPIRAL = 1001

def square_size(n: int) -> int:
    return n ** 2

def move(x, y, direction):
    dx, dy = direction
    x = x + dx
    y = y + dy
    return (x, y)

def rotate(direction):
    dx, dy = direction
    return (-dy, dx)

def solve() -> int:
    size = EDGE_SIZE_OF_SPIRAL
    grid = [[0] * size for _ in range(size)]
    x = y = size // 2
    grid[y][x] = 1
    n = 1
    side_length = 1
    direction = (1, 0)
    while n < size * size:
        for _ in range(2):
            for _ in range(side_length):
                if n == size * size:
                    break
                x, y = move(x, y, direction)
                n += 1
                grid[y][x] = n
            direction = rotate(direction)
        side_length += 1
    return sum(grid[i][i] + grid[i][size - 1 - i] for i in range(size)) - 1


def main():
    print(solve())


if __name__ == "__main__":
    main()
