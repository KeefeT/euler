
def main():
    
    f = 1
    print(len(fibonacci_iterative()) - 1)

def fibonacci_iterative():
    fib_sequence = [0, 1]
    while len(str(fib_sequence[-1])) < 1000:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

if __name__ == "__main__":
    main()