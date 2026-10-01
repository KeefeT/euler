from libeuler.primes import sieve
LIMIT = 1_000_000

def solve() -> int:
    primes = sieve(LIMIT - 1)
    prime_set = set(primes)
    prefix = [0]
    for prime in primes:
        prefix.append(prefix[-1] + prime)
    best_length = 0
    best_prime = 0
    for start in range(len(primes)):
        if start + best_length + 1 > len(primes):
            break
        for end in range(start + best_length + 1, len(primes) + 1):
            total = prefix[end] - prefix[start]
            if total >= LIMIT:
                break
            if total in prime_set:
                best_length = end - start
                best_prime = total
    return best_prime


def main():
    print(solve())


if __name__ == "__main__":
    main()
