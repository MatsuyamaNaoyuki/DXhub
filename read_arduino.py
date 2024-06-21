import serial
import csv
import time
import numpy as np
from datetime import datetime


class bending_sensor:
    def __init__(self):
        self.rowvalue = ''
        self.resistance_value = np.empty(4)

    def get_value(self):
        arduino = serial.Serial('COM3', 115200, timeout=1)
        arduino.reset_input_buffer()  # 入力バッファをクリア
        arduino.reset_output_buffer()  # 出力バッファをクリア
        #くるまで待つを実装する必要がある
        while arduino.in_waiting < 0:
           pass 
        self.rowvalue = arduino.readline().decode('utf-8', errors='ignore').rstrip()
    
    def change_data(self):
        split_value = np.array(self.rowvalue.split('/'))
        float_value = np.asarray(split_value, dtype=float)
        Vcc = 5.0
        Rt = 1000
        for i in range(len(float_value)):
            Vx = float_value[i] * Vcc / 1024
            self.resistance_value[i] = Rt / (Vcc - Vx) * Vx





bending1 = bending_sensor()
bending1.get_value()
bending1.change_data()
print(bending1.resistance_value)
