from pathlib import Path
import math

def solve_exact() -> int:
    largest = -1
    largest_line = 1
    largest_base = -1
    largest_exp = -1
    line_num = 1
    with open(Path(__file__).with_name('0099_base_exp.txt')) as file:
        for line in file:
            arr = line.split(',')
            base = int(arr[0])
            exp = int(arr[1])
            if base < largest_base and exp < largest_exp:
                line_num = line_num + 1
                continue
            n = compute_exponent(base, exp)
            if n > largest:
                largest = n
                largest_line = line_num
                largest_base = base
                largest_exp = exp
            line_num = line_num + 1
    return largest_line

def compute_exponent(base, exp) -> int:
    l = []
    binary_exp = bin(exp)[2:]
    binary_exp = binary_exp[::-1]
    for idx in range(0, len(binary_exp)):
        if binary_exp[idx] == '1':
            l.append(pow(2, idx))
    max = int(l[-1])
    powers = []
    i = 1
    while i <= max:
        powers.append(pow(base, i))
        i = i * 2
    exponent = 1
    for idx in range(0, len(binary_exp)):
        if binary_exp[idx] == '1':
            exponent = exponent * powers[idx]
    return exponent

def compute_by_log():
    base_exponent_pairs = []
    with open(Path(__file__).with_name('0099_base_exp.txt')) as file:
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
    return i_max


def solve() -> int:
    return compute_by_log()


def main():
    print(solve())


if __name__ == "__main__":
    main()
