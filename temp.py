import socket
import struct
import sys,os, time, datetime, csv
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from myclass.MyDynamixel2 import MyDynamixel
# from myclass.MotionCapture2 import MotionCapture
from myclass import myfunction
from myclass.MyMagneticSensor import MagneticSensor

import pandas as pd
import torch

# CSV ファイルを読み込み
csv_file_path = "dami-.csv"
data = myfunction.read_csv_to_torch(csv_file_path)

normalized_data = data.copy()
normalized_data["column_name"] = (data["column_name"] - data["column_name"].min()) / (data["column_name"].max() - data["column_name"].min())
print(normalized_data)






