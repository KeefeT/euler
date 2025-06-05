def main():
    print("start")
    arr = []
    max = -1

    # fill number into array
    with open("resources/problem8-number.txt") as file:
        for line in file:
            for num in line:
                if num != '\n':
                    arr.append(int(num))

    # shitty iterator 
    start = 0

    while start+13 < 1001:
        temp = 1
        for i in range(start, start+13):
            if arr[i] == 0:
                break
            temp *= arr[i]

        if temp > max:
            max = temp

        start += 1

    print("max value: " + str(max))

if __name__ == "__main__":
    main()