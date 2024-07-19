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

path = r'C:\Users\shigf\Program\DXhub\nosensor_Mc20240719_104116.csv'
myfunction.make_3D_graph(path)