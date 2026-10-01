###
#
# By listing the first six prime numbers: 
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10,001st prime number?
#
###

import math

# sieve moment?
def main():

    n = 10001 #th prime
    # https://math.stackexchange.com/questions/1270814/bounds-for-n-th-prime
    upper_bound = int(n * (math.log(n) + math.log(math.log(n))))
    print(upper_bound)

    l = list(range(3, upper_bound, 2)) # quick trick to cut number of
                               # elements in half to start out with

    sieve(l)
    l.insert(0, 2)

    print(l)
    print('\n')
    print(l[10000])


def sieve(l :list) -> list:

    count = 0

    while count < len(l):
        x = l[count]
        y = l[count]

        while y+x <= l[-1]:
            y = y+x
            try:
                l.remove(y)
            except Exception as e:
                continue

        count += 1

if __name__ == "__main__":
    main()