"""Count letters in British number names from one through one thousand."""

LIMIT = 1000
ONES = ("", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen")
TENS = ("", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety")


def stringify(n: int) -> str:
    if not 1 <= n <= 1000:
        raise ValueError("expected a number from 1 to 1000")
    if n == 1000:
        return "one thousand"
    if n >= 100:
        hundreds, remainder = divmod(n, 100)
        words = ONES[hundreds] + " hundred"
        return words + " and " + stringify(remainder) if remainder else words
    if n >= 20:
        tens, ones = divmod(n, 10)
        return TENS[tens] + ("-" + ONES[ones] if ones else "")
    return ONES[n]


def solve() -> int:
    return sum(len(stringify(n).replace(" ", "").replace("-", ""))
               for n in range(1, LIMIT + 1))


def main():
    print(solve())


if __name__ == "__main__":
    main()
