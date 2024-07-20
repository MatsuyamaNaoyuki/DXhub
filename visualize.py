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
def split_to_sublists(row):
    return [row[i:i+3].tolist() for i in range(0, len(row), 3)]

def culc_distance(coordinate1, coordinate2):
    dis = 0
    for i in range(len(coordinate1)):
        dis = dis + (coordinate1[i] - coordinate2[i]) ** 2
    return dis

# def align_origin(path, ave):
#     df = pd.read_csv(path, header=None)
#     df = df.drop(df.columns[0], axis=1)  
#     new_df = df.apply(split_to_sublists, axis=1)
#     coordinate = np.array(new_df.tolist())
#     coordinate = np.ma.masked_where(np.isnan(coordinate), coordinate)
#     coordinate = coordinate - ave
#     return coordinate

def read_coordinate(path):
    df = pd.read_csv(path, header=None)
    df = df.drop(df.columns[0], axis=1)  
    new_df = df.apply(split_to_sublists, axis=1)
    coordinate = np.array(new_df.tolist())
    # print(type(coordinate))

    return coordinate


def get_avereage(coordinate):
    random_values = random.sample(range(1, coordinate.shape[0]), 10)
    pairs = [(random_values[i], random_values[i+1]) for i in range(0, len(random_values), 2)]

    min = []
    for randomval in pairs:
        if np.any(np.isnan(coordinate[randomval[0]])):
            continue
        if np.any(np.isnan(coordinate[randomval[1]])):
            continue

        min_dis = [100000, 1000000]
        temp_min_pair = [[coordinate[1][1],coordinate[1][1]],[coordinate[1][1],coordinate[1][1]]]
        for i in range(coordinate.shape[1]):
            for j in range (coordinate.shape[1]):
                temp = culc_distance(coordinate[randomval[0]][i], coordinate[randomval[1]][j])
                if min_dis[0] > temp:
                    min_dis[1] = min_dis[0]
                    min_dis[0] = temp
                    temp_min_pair[1] = temp_min_pair[0]
                    temp_min_pair[0] = [coordinate[randomval[0]][i], coordinate[randomval[1]][j]]
                elif min_dis[1] > temp:
                    min_dis[1] = temp
                    temp_min_pair[1] = [coordinate[randomval[0]][i], coordinate[randomval[1]][j]]

        
        if temp_min_pair[0][0][2] > temp_min_pair[1][0][2]:
            min.append(temp_min_pair[0])
        else:
            min.append(temp_min_pair[1])


    min_list = [list(i) for i in min]
    final_average = np.mean(min_list, axis=0)
    final_average = np.mean(final_average, axis=0)
    return final_average
    print(final_average)







path = r'C:\Users\shigf\Program\DXhub\sensor_Mc20240719_113028.csv'

coordinate = read_coordinate(path)
avereage = get_avereage(coordinate)
new = coordinate - avereage
np.set_printoptions(suppress=True)
print(new)


# df = pd.read_csv(path)
# df = df.drop(df.columns[0], axis=1)  
# new_df = df.apply(split_to_sublists, axis=1)
# coordinate = np.array(new_df.tolist())
# ave = 0
# for i in range(10):
#     ave = ave + coordinate[i][5][:]
# ave = ave / 10
# print(ave)
# coordinate = align_origin(path, ave)
# myfunction.make_3D_graphs(coordinate)

# # print(coordinate)


