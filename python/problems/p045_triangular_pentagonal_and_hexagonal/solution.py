import math


def triangle(n: int) -> int:
    t = n * (n + 1) // 2
    return t

def pentagonal(n: int) -> int:
    p = n * (3 * n - 1) // 2
    return p

def hexagonal(n: int) -> int:
    h = n * (2 * n - 1)
    return h

def solve() -> int:
    # Every hexagonal number is triangular; check whether it is pentagonal too.
    n = 144
    while True:
        value = hexagonal(n)
        discriminant = 24 * value + 1
        root = math.isqrt(discriminant)
        if root * root == discriminant and (1 + root) % 6 == 0:
            return value
        n += 1


def main():
    print(solve())


if __name__ == "__main__":
    main()
