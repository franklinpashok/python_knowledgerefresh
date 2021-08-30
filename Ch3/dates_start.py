#Example file for working with dates

from datetime import date
from datetime import time
from datetime import datetime

def main():

#DATE Objects
# Get todays date from simple today
    today = date.today()
    print("Today's date is", today)
#printout dates individual components
    print("Date Components:", today.day, today.month, today.year)

#retrieve today's weekday (0=Monday, 6=Sunday)
    print("Today weekday number is: ", today.weekday())
    days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    print("which is a:", days[today.weekday()])

#DATE Time Objects
    today = datetime.now()
    print("the current date and time: ", today)
    t = datetime.time(datetime.now())
    print(t)

if __name__ == "__main__":
    main()