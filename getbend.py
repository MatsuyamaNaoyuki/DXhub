import sys,os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting
import csv
import pprint
from myclass import MyDynamixel


def check_bend(Motors):
    print("A")
    for j in (3, 1, 2):
        for i in range(300):
            Motors.move(j,i)
            time.sleep(0.1)
            if i % 100 == 0:
                time.sleep(5)
        for i in reversed(range(0, 300)):
            Motors.move(j,i)
        Motors.back_to_initial_position()
    
    



filename = 'nosensor'

Motors = MyDynamixel()
# Motors.manual_move()
# Motors.back_to_initial_position()

check_bend(Motors)

now = datetime.datetime.now()
filename = os.path.dirname(__file__) +"\\" + filename + now.strftime('%Y%m%d_%H%M%S') + '.csv'

with open(filename, 'w',newline="") as f:
    writer = csv.writer(f)
    writer.writerows(Motors.anglerecord)

# Motors.manual_move()
# forces = Motors.get_present_PWMs()
# print(forces)
# Motors.back_to_initial_position()
# angles = Motors.get_present_angles()
# print(angles)


