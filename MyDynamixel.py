import sys, time
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting

class MyDynamixel():
    def __init__(self):
        self.IDs = (ctypes.c_uint8 * 4)(1,2,3,4)
        self.dev = dx2.DX2_OpenPort(setting.COMPort, setting.Baudrate)
        #ID一覧分のDynamixelをMultiTurnモード=4に変更
        dx2.DXL_SetOperatingModesEquival(self.dev, self.IDs, len(self.IDs), 4)
        # ID一覧分のDynamixelをトルクディスエーブル
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), True)

    def back_to_initial_position(self):
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), False)
        time.sleep(3)
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), True)
        for id in range(self.IDs):
            nowPWM = (ctypes.c_double)()
            dx2.DXL_GetPresentPWM(self.dev, id, nowPWM)
            while nowPWM > 1:
                self.move(id, 5)
            
        #力がかかるまでmove
        #少し緩める


    def move(self, id, ):
        

    def measurement_rotation_angle():

    def measurement_force():