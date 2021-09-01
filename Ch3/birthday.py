import datetime
from datetime import date
import calendar
from datetime import timedelta

def main():

    today=date.today()
    m = input("Your Birthday Month Choose between 1-12:")
    d = input("Your Birthday date:")
    bday=date(today.year,int(m),int(d))
    diff = (bday-today).days
    #diff = diff+365
    if diff > 0:
        print("You Birthday is in", diff, "days")
    else:
        print ("birthday is in over")

if __name__ == "__main__":
    main()
