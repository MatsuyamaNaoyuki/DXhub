import sys,os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), 'myclass'))
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting
import csv
import pprint
from myclass.MyDynamixel2 import MyDynamixel
from myclass.MotionCapture2 import MotionCapture
from myclass.MyBendingSensor import BendingSensor
from myclass import myfunction
import numpy as np

BC = BendingSensor()

for i in range(10):
    data = BC.get_value()
    print(data)