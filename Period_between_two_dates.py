#Write a Python program to calculate number of days between two dates.
#Sample dates : (2014, 7, 2), (2014, 7, 11)
#Expected output : 9 days

import datetime

d1=datetime.date(2014,7,11)
d2=datetime.date(2014,7,2)

#num_days=d1[2]-d2[2]
#print(num_days)

d=d1-d2
print(d.days)