###
#
# 2520 is the smallest number that can be divided by - 
# each of the numbers from 1 to 10 without any remainder.
# 
# What is the smallest positive number that is evenly -
# divisible by all of the numbers from 1 to 20?
#
###

import timeit

def quick():
    count = 2520 # has to be divisible by 20, 2520 is 1-10 and %20
    nums = [11, 13, 14, 16, 17, 18, 19] # don't include 20 cause we guarantee that with count
    # 20 = 4x5
    # 18 = 3x6
    # 16 = 4x4
    # 15 = 3x5 -- already taken care of by 20 and 18
    # 14 = 2x7
    # 12 = 2x6, 3x4 -- already taken care of by 20 and 18 

    # can remove 
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 20
    while True:
        x = True
        for i in nums:
            if (count % i) != 0:
                x = False
                break
        if x:
            print(count)  
            return
        count += 2520 # !!!

def slow():
    count = 22 # has to be divisible by 20
    while True:
        x = True
        for i in range(3, 20): # works but shitty but slow.... only need to check 3-20? 3-20 and not 10?
            if (count % i) != 0:
                x = False
                break
        if x:
            print(count)  
            return
        count += 2 # count has to be even

if __name__ == "__main__":

    elapsed_time_quick = timeit.timeit(quick, number=1)
    print(f"Elapsed time for quick: {elapsed_time_quick:.2f} seconds")

    elapsed_time_slow = timeit.timeit(slow, number=1)
    print(f"Elapsed time for quick: {elapsed_time_slow:.2f} seconds")

    print(f"Increase: {elapsed_time_slow/elapsed_time_quick:.2f}x faster")