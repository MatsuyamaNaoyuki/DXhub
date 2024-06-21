import serial
import csv
import time
from datetime import datetime


class bending_sensor:
    def __init__(self):
        self.value = ''

    def get_value(self):
        arduino = serial.Serial('COM3', 115200, timeout=1)
        arduino.reset_input_buffer()  # 入力バッファをクリア
        arduino.reset_output_buffer()  # 出力バッファをクリア
        #くるまで待つを実装する必要がある
        while arduino.in_waiting < 0:
           pass 
        self.value = arduino.readline().decode('utf-8', errors='ignore').rstrip()
        print(self.value)



bending1 = bending_sensor()
bending1.get_value()
print(bending1.value)
# while True:
#     if arduino.in_waiting > 0:
#         val_arduino = arduino.readline().decode('utf-8', errors='ignore').rstrip()
# 	    #val_decoded = float(repr(val_arduino.decode())[1:-5])
#         data = val_arduino.split('/')
#         print(data)
# ser.close()