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




file_path = r'C:\Users\shigf\Program\DXhub\sensor_Mc20240719_113028.csv'

data = []

# CSVファイルを読み込む
with open(file_path, 'r') as file:
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        # 最初の列は日付データとして保持し、それ以外の列は数値に変換
        date = row[0]
        values = [float(value) for value in row[1:]]
        data.append([date] + values)

# データをNumPy配列に変換（数値部分のみ）
numeric_data = np.array([row[1:] for row in data])

# 日付データを表示
print("Date data:")
for row in data:
    print(row[0])

# 数値データを表示
print("\nNumeric data:")
print(numeric_data)