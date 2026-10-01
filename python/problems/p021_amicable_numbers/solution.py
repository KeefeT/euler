LIMIT = 10000

def proper_divisors_sum(n: int) -> int:
    if n <= 1:
        return 0
    total = 1
    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            total += divisor
            other = n // divisor
            if other != divisor:
                total += other
    return total

def solve() -> int:
    amicable = set()
    for n in range(2, LIMIT):
        partner = proper_divisors_sum(n)
        if partner != n and proper_divisors_sum(partner) == n:
            amicable.add(n)
    return sum(amicable)


def main():
    print(solve())


if __name__ == "__main__":
    main()
