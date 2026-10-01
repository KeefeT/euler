
from datetime import date, timedelta

def main():
    d = date(1901, 1, 1)
    dt = timedelta(days=1)
    end = date(2000, 12, 31)

    sundays = 0

    while d != end:
        if d.strftime("%A") == "Sunday" and d.day == 1:
            print(f"Found a Sunday! {d}")
            sundays = sundays + 1
        d = d + dt

    print(f'Sundays: {sundays}')




if __name__ == "__main__":
    main()