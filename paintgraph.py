import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta, timezone
import time

# CSVファイルのパスを指定
csv_file_path = 'MoldStar2kaime.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path, header=None)




# 読み込んだデータの確認（最初の5行を表示）
print(df.head())

first_time = df[0][0]
first_time = datetime.strptime(first_time, "%Y-%m-%d %H:%M:%S.%f")


for i in range(len(df)):
    tmptime = datetime.strptime(df[0][i],  "%Y-%m-%d %H:%M:%S.%f")
    seconds = tmptime - first_time
    milliseconds = seconds.total_seconds() * 1000
    df[0][i] = milliseconds



    
print(df)

# グラフを作成する列を指定（例として 'Column1' と 'Column2' を使用）
# 実際の列名に置き換えてください
# 例えば、1列目のデータをプロットする場合
# 複数の列をプロット（例として1列目、2列目、3列目をプロット）
x_values = df[0]  # 横軸はデータ数（インデックス）
y_values_1 = df[1]  # 1列目
y_values_2 = df[2]  # 2列目
y_values_3 = df[3]  # 3列目

y_values_4 = df[4]  # 1列目
y_values_5 = df[5]  # 2列目
y_values_6 = df[6]  # 3列目

y_values_7 = df[7]  # 1列目
y_values_8 = df[8]  # 2列目
y_values_9 = df[9]  # 3列目

# グラフを作成
plt.figure(figsize=(10, 6))

# 各列をプロット
plt.plot(x_values, y_values_1, label='top left values')
plt.plot(x_values, y_values_2, label='top sentor values')
plt.plot(x_values, y_values_3, label='top right values')
plt.plot(x_values, y_values_4, label='sentor left values')
plt.plot(x_values, y_values_5, label='sentor sentor values')
plt.plot(x_values, y_values_6, label='sentor right values')
# plt.plot(x_values, y_values_7, label='root left values')
# plt.plot(x_values, y_values_8, label='root sentor values')
# plt.plot(x_values, y_values_9, label='root right values')

# グラフのタイトル、ラベル、凡例を設定
plt.title('big sand2')
plt.xlabel('milisecond')
plt.ylabel('sensor Value')

plt.ylim(580,700)


# 凡例を表示
plt.legend()

# グラフを表示
plt.show()