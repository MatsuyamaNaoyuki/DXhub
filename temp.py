from datetime import datetime

# 2つの時刻をdatetimeオブジェクトに変換
time_str1 = "2024-10-03 14:40:33.505496"
time_str2 = "2024-10-03 14:30:33.505496"

time_obj1 = datetime.strptime(time_str1, "%Y-%m-%d %H:%M:%S.%f")
time_obj2 = datetime.strptime(time_str2, "%Y-%m-%d %H:%M:%S.%f")

# 時刻の差を計算（timedeltaオブジェクト）
time_difference = time_obj1 - time_obj1

# timedeltaをミリ秒に変換
milliseconds_difference = time_difference.total_seconds() * 1000

# 結果の出力
print(f"時刻の差: {milliseconds_difference} ミリ秒")