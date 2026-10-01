import unittest
from unittest.mock import patch

from libeuler.primes import sieve
from problems.p037_truncatable_primes import solution


class TruncatablePrimeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.primes = set(sieve(1_000_000))

    def test_truncatable_primes(self):
        expected = {23, 37, 53, 73, 313, 317, 373, 797, 3137, 3797, 739397}
        with patch.object(solution, 'PRIMES', self.primes):
            for prime in expected:
                with self.subTest(prime=prime):
                    self.assertTrue(solution.isTruncatable(prime))

    def test_other_numbers_are_not_truncatable(self):
        expected = {23, 37, 53, 73, 313, 317, 373, 797}
        with patch.object(solution, 'PRIMES', self.primes):
            for n in range(1, 1000):
                if n not in expected:
                    with self.subTest(n=n):
                        self.assertFalse(solution.isTruncatable(n))

    def test_repeated_solve_has_the_same_answer(self):
        self.assertEqual(solution.solve(), 748317)
        self.assertEqual(solution.solve(), 748317)


if __name__ == '__main__':
    unittest.main()
