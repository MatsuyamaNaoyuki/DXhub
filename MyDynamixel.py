import sys, time
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting

class MyDynamixel():
    def __init__(self):
        self.IDs = (ctypes.c_uint8 * 4)(1,2,3,4)
        self.dev = dx2.DX2_OpenPort(setting.COMPort, setting.Baudrate)
        if self.dev != None:
            # ID一覧分のDynamixelを検索しモデルp名を表示
            for id in self.IDs:
                print(id, dx2.DXL_GetModelInfo(self.dev,id).contents.name.decode())
        else:
            print('Could not open COM port.')
        #ID一覧分のDynamixelをMultiTurnモード=4に変更
        dx2.DXL_SetOperatingModesEquival(self.dev, self.IDs, len(self.IDs), 4)
        # ID一覧分のDynamixelをトルクディスエーブル
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), True)
        self.rotation_angles = (ctypes.c_double * len(self.IDs))()
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.rotation_angles, len(self.IDs))



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


    def move(self, id, angle_displacement):
        idi = id - 1
        gole_angles = self.rotation_angles

        #方向の調整
        if id == 1 or 4:
            setangle = angle_displacement * -1
        else:
            setangle = angle_displacement

        gole_angles[idi] = gole_angles[idi] + setangle
        dx2.DXL_SetGoalAngles (self.dev, self.IDs,  gole_angles, len(self.IDs))
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.rotation_angles, len(self.IDs))


    def printAngle(self):

        print('(', end='')
        print(('{:7.1f},'*len(self.rotation_angles)).format(*self.rotation_angles), end=')\n')

        

    # def measurement_rotation_angle():

    # def measurement_force():

Motors = MyDynamixel()
# Motors.printAngle()
Motors.move(4, 100)

