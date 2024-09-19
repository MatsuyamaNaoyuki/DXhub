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
from myclass import myfunction
import pandas as pd
import numpy as np
import random

def swap(a, b):
    return b,a

path = r'C:\Users\shigf\Program\DXhub\sensor_Mc20240719_113028.csv'

sensorcoordinate = myfunction.read_coordinate(path)
sensoravereage = myfunction.get_avereage(sensorcoordinate)
sensornew = sensorcoordinate - sensoravereage
np.set_printoptions(suppress=True)

path = r'C:\Users\shigf\Program\DXhub\nosensor_Mc20240719_104116.csv'

nosensorcoordinate = myfunction.read_coordinate(path)
nosensoravereage = myfunction.get_avereage(nosensorcoordinate)
nosensornew = nosensorcoordinate - nosensoravereage
sensornew[11][0], sensornew[11][5] = sensornew[11][5].copy(), sensornew[11][0].copy()
sensornew[11][4], sensornew[11][1] = sensornew[11][1].copy(), sensornew[11][4].copy()
sensornew[11][3], sensornew[11][2] = sensornew[11][2].copy(), sensornew[11][3].copy()
sensornew[11][4], sensornew[11][5] = sensornew[11][5].copy(), sensornew[11][4].copy()
nosensornew[11][0], nosensornew[11][5] = nosensornew[11][5].copy(), nosensornew[11][0].copy()
nosensornew[11][4], nosensornew[11][1] = nosensornew[11][1].copy(), nosensornew[11][4].copy()
# nosensornew[11][3], nosensornew[11][2] = nosensornew[11][2].copy(), nosensornew[11][3].copy()
nosensornew[11][4], nosensornew[11][5] = nosensornew[11][5].copy(), nosensornew[11][4].copy()
coor = np.array([sensornew[11], nosensornew[11]])
print(coor)
np.set_printoptions(suppress=True)
myfunction.make_3D_graphs(coor,labelname=["sensor", "nosensor"] ,lineswitch= True)