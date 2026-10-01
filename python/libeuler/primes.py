"""Prime number helpers."""


def sieve(limit: int) -> list[int]:
    if limit < 2:
        return []

    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False

    for p in range(2, int(limit**0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, limit + 1, p):
                is_prime[multiple] = False

    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes
