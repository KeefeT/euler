###
#
# The sum of the squares of the first ten natural numbers is,
# 1^2 + 2^2 + ... + 10^2 = 385
# 
# The square of the sum of the first ten natural numbers is,
# (1+2+...+10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first-
# ten natural numbers and the square of the sum is 
# 3025-385=2640
#
# Find the difference between the sum of the squares of the first-
# one hundred natural numbers and the square of the sum.
#
###


def sum_of_squares(limit: int) -> int:
    sum = 0
    for i in range(1, limit+1):
        sum += i*i
    return sum

def square_of_sum(limit: int) -> int:
    sum = 0
    for i in range (1, limit+1):
        sum += i
    return sum*sum

def main():
    limit = 100
    diff = square_of_sum(limit) - sum_of_squares(limit)
    print(f"diff: {diff}")

if __name__ == "__main__":
    main()