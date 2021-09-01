# #
# #Example file for working with calenders
# #

# #import the calender module - the below statement imports all various classes of calender module 
import calendar
from datetime import date, datetime
from time import strftime

# # create a plain text calender
# c = calendar.TextCalendar(calendar.SUNDAY)
# st = c.formatmonth(2021, 9, 0, 0)
# print(st)

# # create a html formatted calender
# hc = calendar.HTMLCalendar(calendar.SUNDAY)
# ht = hc.formatmonth(2021, 9)
# print(ht)

# #loop over the days of a month
# # zero output means the day of a week from another month
# for i in c.itermonthdays(2021, 9):
#     print(i)

# # calender modules provides useful utilities like the month name and day name
# for name in calendar.month_name:
#     print(name)
# for day in calendar.day_name:
#     print(day)

# # calculate based on a rule: 
# # a team meeting on the first friday of everymonth
# # figure out what days that would be for each month

def main():

    for m in range (1,13):
        cal = calendar.monthcalendar(2021, m)
        weekone = cal[0]
        weektwo = cal[1]

        if weekone[calendar.FRIDAY] != 0:
            meetday = weekone[calendar.FRIDAY]
        else:
            meetday = weektwo[calendar.FRIDAY]
    
        print(meetday, calendar.month_name[m], strftime("%Y"))

if __name__ == '__main__':
    main()