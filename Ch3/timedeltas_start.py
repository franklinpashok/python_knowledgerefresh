#
# time delats
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

# construct a basic time delta

print(timedelta(days=365, hours=5, minutes=1))

now = datetime.now()
# print today's date
print("today is:" + str(now))
#print date one year from now
print("one year from now it will be:" + str(now + timedelta(weeks=52)))
# print date one year before
print("one year before it was:" + str(now - timedelta(weeks=52)))