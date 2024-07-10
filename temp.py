
import sys, time, datetime
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting
import csv
import pprint


i = [0,0,0,0]
now_time  = datetime.datetime.now()

a = []
i.insert(0, now_time)
a.append(i)
a.append(i)

with open('C:\\Users\\shigf\\Program\\DXhub\\data\\sample_writer.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(a)


print(a)