###
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is
# 9009 = 91 x 99
# Find the largest palindrome made from the product of two 3-digit numbers.
#
###

def main():
    max = -1
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            s = str(i*j)

            if s == s[::-1]:
                if int(s) > max:
                    max = int(s)

    print("solution: " + str(max))

if __name__ == "__main__":
    main()