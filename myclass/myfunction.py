import sys,os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), 'myclass'))
import ctypes
import csv
import pprint
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
import numpy as np


def make_3D_graph(path):
    df = pd.read_csv(path)
    df = df.drop(df.columns[0], axis=1)     #時間を削除
    rows = df.iloc[12:18]
    print(rows)
    # 3次元の散布図を作成
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # カラーマップを使って色を設定
    colors = plt.cm.jet(np.linspace(0, 1, len(rows)))

    # 各行のデータをプロット
    for i, row in enumerate(rows.iterrows()):
        first_row = row[1]
        x = first_row[::3]
        y = first_row[1::3]
        z = first_row[2::3]
        ax.scatter(x, y, z, c=colors[i], marker='o', label=f'Row {i+1}')

    ax.set_xlim(0,250)
    ax.set_ylim(0,250)
    ax.set_zlim(0,250)

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    ax.legend()

    plt.show()

# path = r'C:\Users\shigf\Program\DXhub\myclass\test20240719_092125.csv'
# make_3D_graph(path)