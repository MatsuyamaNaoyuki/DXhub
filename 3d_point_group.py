import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ランダムな三次元点群データを生成
# points = np.array([[ 0.02450288,  0.29230633,  0.07552876],
#                    [ 0.05023039,  0.3165764 ,  0.11971987],
#                    [-0.02856168,  0.33669937,  0.18210588],
#                    [ 0.0260123 ,  0.3378214 ,  0.16765516],
#                    [-0.07354284,  0.3155185 ,  0.15206835]])


points = np.array([[ 0.02450288,  0.29230633,  0.07552876],
                   [ 0.05023039,  0.3165764 ,  0.11971987],
                   [ 0.0260123 ,  0.3378214 ,  0.16765516],
                   [-0.02856168,  0.33669937,  0.18210588],
                   [-0.07354284,  0.3155185 ,  0.15206835]])
# 3Dプロットの作成
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 点群を線でつなぐ（折れ線グラフ）
ax.plot(points[:, 0], points[:, 1], points[:, 2], color='b', marker='o', linestyle='-')

# 軸ラベル
ax.tick_params(axis='x', labelsize=0)
ax.tick_params(axis='y', labelsize=0)
ax.tick_params(axis='z', labelsize=0)


# 表示
plt.show()