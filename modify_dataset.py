import csv
from myclass import myfunction

# CSVファイルを開く
data = []
with open('margedata20241203_171240.csv', mode='r', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

max_length = max(len(row) for row in data)

print(max_length)
# 最大長に満たない行を削除
filtered_data = [row for row in data if len(row) == max_length]


filtered_data = [row for row in filtered_data if '' not in row]

filtered_data = [
    row for idx, row in enumerate(filtered_data)
    if (idx == 0) or all(500 <= int(row[i]) <= 800 for i in range(9, 18))  # 1行目は条件をスキップ
]
myfunction.wirte_csv(filtered_data, "test")