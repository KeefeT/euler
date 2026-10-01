import unittest

from libeuler.primes import sieve


class SieveTests(unittest.TestCase):
    def test_limits_below_two(self):
        for limit in (-10, 0, 1):
            with self.subTest(limit=limit):
                self.assertEqual(sieve(limit), [])

    def test_includes_prime_limit(self):
        self.assertEqual(sieve(2), [2])
        self.assertEqual(sieve(13), [2, 3, 5, 7, 11, 13])

    def test_excludes_composites_and_prime_squares(self):
        self.assertEqual(sieve(25), [2, 3, 5, 7, 11, 13, 17, 19, 23])


if __name__ == "__main__":
    unittest.main()
