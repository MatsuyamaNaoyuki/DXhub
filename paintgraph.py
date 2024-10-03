import pandas as pd
import matplotlib.pyplot as plt

# CSVファイルのパスを指定
csv_file_path = 'MagChack20240930_164218.csv'

# CSVファイルを読み込む
df = pd.read_csv(csv_file_path, header=None)

# 読み込んだデータの確認（最初の5行を表示）
print(df.head())

# グラフを作成する列を指定（例として 'Column1' と 'Column2' を使用）
# 実際の列名に置き換えてください
# 例えば、1列目のデータをプロットする場合
# 複数の列をプロット（例として1列目、2列目、3列目をプロット）
x_values = range(len(df))  # 横軸はデータ数（インデックス）
y_values_1 = df[0]  # 1列目
y_values_2 = df[1]  # 2列目
y_values_3 = df[2]  # 3列目

# グラフを作成
plt.figure(figsize=(10, 6))

# 各列をプロット
plt.plot(x_values, y_values_1, label='Column 0 values')
plt.plot(x_values, y_values_2, label='Column 1 values')
plt.plot(x_values, y_values_3, label='Column 2 values')

# グラフのタイトル、ラベル、凡例を設定
plt.title('Plot of Multiple Columns vs Index')
plt.xlabel('Index (Count)')
plt.ylabel('Column values')

# 凡例を表示
plt.legend()

# グラフを表示
plt.show()