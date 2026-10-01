###
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143?
###
import math

def solve() -> int:
    target = 600851475143
    max_potential_prime = int(math.sqrt(target))
    primes = [1] #...

    for i in range(3, max_potential_prime, 2): # iterate by 2, even's never prime
        if (target % i) == 0:
            #if num is a factor of target
            x = True
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if (i % j) == 0:
                    # not a prime
                    x = False
                    break
            if x:
                primes.append(int(i))

    return max(primes)


def main():
    print(solve())


if __name__ == "__main__":
    main()
