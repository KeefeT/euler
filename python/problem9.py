###
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, 
# a^2 + b^2 = c^2
#
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000
# Find the product abc
#
###


def main():

    triplets = []

    find_triplets(triplets)

    print(triplets)

    special = find_special_pythagorean_triplet(triplets)

    print(special)

    product = special[0] * special[1] * special[2]

    print(product)
    

def find_triplets(t: list) -> list:

    for a in range(1, 500): # a < b < c, a+b+c=1000, therefore a < 500
        for b in range(a, 500):
            for c in range(b, 500):
                if ((a*a) + (b*b)) == (c*c):
                    t.append((a, b, c)) # could just do the check a+b+c = 1000 here
                                        # but I kinda wanted to compute the whole list 
                    print(t[-1])
    return t

def find_special_pythagorean_triplet(l: list) -> tuple:
    for t in l:
        a = t[0]
        b = t[1]
        c = t[2]

        if (a+b+c) == 1000:
            return t


if __name__ == "__main__":
    main()