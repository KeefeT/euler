###
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23
# Find the sum of all the multiples of 3 or 5 below 1000
###

def solve() -> int:
    primes = [3, 5]
    sum = 0

    for i in range(1, 1000):
        for p in primes:
            if (i % p) == 0:
                #print(str(i) + " is divisible by " + str(p) + "!")
                sum += i
                break

    return sum


def main():
    print(solve())


if __name__ == "__main__":
    main()
