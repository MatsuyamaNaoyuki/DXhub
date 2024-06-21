import serial
import csv
import time
from datetime import datetime




arduino = serial.Serial('COM3', 115200, timeout=1)
arduino.reset_input_buffer()  # 入力バッファをクリア
arduino.reset_output_buffer()  # 出力バッファをクリア
# 現在の日時を取得してファイル名に埋め込む
# current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
# csv_file = f'sensor_data_{current_time}.csv'            #fstringを用いて文字列に変数を埋め込む



while True:
	val_arduino = arduino.readline()
	
	#val_decoded = float(repr(val_arduino.decode())[1:-5])
	print(val_arduino)
ser.close()