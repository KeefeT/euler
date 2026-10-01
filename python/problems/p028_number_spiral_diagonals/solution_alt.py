EDGE_SIZE_OF_SPIRAL = 1001

def get_corners_sum(side_length: int):
    if side_length == 1:
        return 1
    square = side_length ** 2
    n = side_length - 1
    sum = 0
    for i in range(0, 4):
        sum += square - i * n
    return sum

def solve() -> int:
    return sum(get_corners_sum(side) for side in range(1, EDGE_SIZE_OF_SPIRAL + 1, 2))


def main():
    print(solve())


if __name__ == "__main__":
    main()
