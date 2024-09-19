import sys,os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), 'myclass'))
import ctypes
import csv
import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np
from scipy.spatial import distance_matrix
import random

# def make_3D_graph(path, firstrow = 1, lastrow = 5):
#     df = pd.read_csv(path)
#     df = df.drop(df.columns[0], axis=1)     #時間を削除
#     rows = df.iloc[firstrow:lastrow]
#     print(rows)
#     # 3次元の散布図を作成
#     fig = plt.figure()
#     ax = fig.add_subplot(111, projection='3d')

#     # カラーマップを使って色を設定
#     colors = plt.cm.jet(np.linspace(0, 1, len(rows)))

#     # 各行のデータをプロット
#     for i, row in enumerate(rows.iterrows()):
#         first_row = row[1]
#         x = first_row[::3]
#         y = first_row[1::3]
#         z = first_row[2::3]
#         ax.scatter(x, y, z, c=colors[i], marker='o', label=f'Row {i+1}')

#     ax.set_xlim(0,250)
#     ax.set_ylim(0,250)
#     ax.set_zlim(0,250)

#     ax.set_xlabel('X Label')
#     ax.set_ylabel('Y Label')
#     ax.set_zlabel('Z Label')
#     ax.legend()

#     plt.show()

def make_3D_graphs(coordinate, labelname = [],  lineswitch= False):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # カラーマップを使って色を設定
    # colors = plt.cm.jet(np.linspace(0, 1, coordinate.shape[0]))
    colors = ["r", "b", "g", "c", "m", "y", "k", "w"]
    # 各行のデータをプロット
    
    if labelname == []:
        for i in range(coordinate.shape[0]):
            labelname.append("label" + str(i+1))
    
    
    if lineswitch == True:
        i = 0
        for coor in coordinate:
            # dist_matrix = distance_matrix(coor, coor)
            # np.fill_diagonal(dist_matrix, np.inf)
            # dist_matrix[np.tril_indices_from(dist_matrix)] = np.inf
            # # min_indices = np.unravel_index(np.argmin(dist_matrix), dist_matrix.shape)
            # min_indices = np.argmin(dist_matrix[:-1], axis=1)
            # print(dist_matrix)
            # print(min_indices)

            for j in range(6):
                x = coor[j][0]
                y = coor[j][1]
                z = coor[j][2]
                if j == 5:
                    ax.scatter(x, y, z, c=colors[i % 8], marker='o', label = labelname[i])
                else:
                    ax.scatter(x, y, z, c=colors[i % 8], marker='o')
            for j in range(1,5): 
                ax.plot([coor[j][0], coor[j+1][0]],
                        [coor[j][1], coor[j+1][1]],
                        [coor[j][2], coor[j+1][2]], c=colors[i % 8])

            i = i +1
    else:
        i = 0
        for coor in coordinate:
            for j in range(6):
                x = coor[j][0]
                y = coor[j][1]
                z = coor[j][2]
                if j == 5:
                    ax.scatter(x, y, z, c=colors[i % 8], marker='o', label = labelname[i])
                else:
                    ax.scatter(x, y, z, c=colors[i % 8], marker='o')
            i = i+1
            
    maxcoors = np.nanmax(coordinate, axis=0)
    maxcoors = np.nanmax(maxcoors, axis=0)
    mincoors = np.nanmin(coordinate, axis=0)
    mincoors = np.nanmin(mincoors, axis=0)  
    difference = maxcoors - mincoors
    maxdifference = np.max(difference)
    center = difference / 2 + mincoors


    ax.set_xlim(center[0] -maxdifference / 2,center[0] + maxdifference / 2)
    ax.set_ylim(center[1] -maxdifference / 2,center[1] + maxdifference / 2)
    ax.set_zlim(center[2] -maxdifference / 2,center[2] + maxdifference / 2)    
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.legend()

    plt.show()



# path = r'C:\Users\shigf\Program\DXhub\myclass\test20240719_092125.csv'
# make_3D_graph(path)
def culc_distance(coordinate1, coordinate2):
    dis = 0
    for i in range(len(coordinate1)):
        dis = dis + (coordinate1[i] - coordinate2[i]) ** 2
    return dis


def split_to_sublists(row):
    return [row[i:i+3].tolist() for i in range(0, len(row), 3)]

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

def merge_list(a, b):
    a = np.array(a)
    b = np.array(b)

    c = np.concatenate((a,b), axis = 1)
    return c