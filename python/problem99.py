import math


def main():
    largest = -1
    largest_line = 1
    largest_base = -1
    largest_exp = -1
    line_num = 1
    with open("./resources/0099_base_exp.txt") as file:
        for line in file:
            print(f'Line num {line_num}')
            arr = line.split(',')
            base = int(arr[0])
            exp = int(arr[1])
            print(f"Calculating {base} to the {exp}!")
            if (base < largest_base and exp < largest_exp):
                print("No way it's this, skipping...")
                line_num = line_num + 1
                continue

            n = compute_exponent(base, exp)
            if n > largest:
                print("Found a bigger one!")
                largest = n
                largest_line = line_num
                largest_base = base
                largest_exp = exp
            line_num = line_num + 1

        print(f'Largest line = {largest_line}')


def compute_exponent(base, exp) -> int:
    l = []
    # get binary form of exponent
    binary_exp = bin(exp)[2:]

    #reverse it to make logic easier
    binary_exp = binary_exp[::-1]

    #iterate through it to find all powers of two to add up
    for idx in range(0, len(binary_exp)):
        if binary_exp[idx] == "1":
            l.append(pow(2,idx))

    max = int(l[-1])

    powers = []
    i = 1
    while i <= max:
        powers.append(pow(base, i))       
        i = i * 2
    
    exponent = 1
    for idx in range(0, len(binary_exp)):
        if binary_exp[idx] == "1":
            exponent = exponent * powers[idx]

    return exponent


def compute_by_log():

    # a1^b1 > a2^b2
    # log(a1^b1) = b1 * log10(a1)
    # log(a2^b2) = b2 * log10(a2)
    # b1 * log10(a1) > b2 * log10(a2)
    # very cool 
 
    base_exponent_pairs = []
    with open("./resources/0099_base_exp.txt") as file:
        for line in file:
            arr = line.split(',')
            base = int(arr[0])
            exp = int(arr[1])
            base_exponent_pairs.append([base, exp])

    max = -1
    i = 1
    i_max = 1

    for pair in base_exponent_pairs:
        n = pair[1] * math.log(pair[0])
        if n > max:
            i_max = i
            max = n
        i = i + 1

    print(i_max)

if __name__ == "__main__":
    main()