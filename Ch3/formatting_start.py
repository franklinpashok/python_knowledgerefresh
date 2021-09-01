#
# Example File for formatting time and date output
#

from datetime import datetime

def main():

# formatting time and date with predefined string control codes

    now = datetime.now()

# %y/%Y - Year, %a/%A - weekday, %b/%B - Month, %d - day of month
    print(now.strftime("The current year is: %Y \nMonth is: %B \nToday is: %A"))
    print(now.strftime("%A - %d-%B-%Y"))
# %c - locale's date and time, %x - locale's date, %X - locale time
    print(now.strftime("local date and time: %c"))
    print(now.strftime("local date: %x"))
    print(now.strftime("local time: %X"))
# time formatting
#    %I/%H - 12/24 Hour, %M - Minute, %S - second, %p - Locale's AM/PM
    print(now.strftime("Current time: %I:%M"))


if __name__ == "__main__":
    main()