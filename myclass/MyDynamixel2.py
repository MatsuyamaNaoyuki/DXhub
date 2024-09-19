import sys,os, time, datetime
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting
import csv
import pprint

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
        self.start_angles = (ctypes.c_double * len(self.IDs))()
        self.force = (ctypes.c_double * len(self.IDs))()
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.start_angles, len(self.IDs))
        self.anglerecord = []



    #初期姿勢に戻る
    def back_to_initial_position(self):
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), False)
        time.sleep(1)
        dx2.DXL_SetTorqueEnablesEquival(self.dev, self.IDs, len(self.IDs), True)
        for id in self.IDs:
            nowforce = self.get_present_PWM(id)
            if nowforce == 0.0:
                dx2.DX2_ClosePort(self.dev)
                self.dev = dx2.DX2_OpenPort(setting.COMPort, setting.Baudrate)
            while nowforce.value < 1:
                self.move(id, 1)
                time.sleep(1)
                nowforce = self.get_present_PWM(id)
                print(id, nowforce.value)
            self.move(id, -1)
        self.start_angles = (ctypes.c_double * len(self.IDs))()
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.start_angles, len(self.IDs))


            
        #力がかかるまでmovep
        #少し緩める

    def get_present_PWM(self, id):
        nowforce = (ctypes.c_double)()
        dx2.DXL_GetPresentPWM(self.dev, id,  nowforce)
        if id == 1 or id == 4:
            nowforce.value = nowforce.value * -1
        return nowforce

    def get_present_PWMs(self):
        nowforce = (ctypes.c_double)()
        nowforces = []
        for id in self.IDs:
            dx2.DXL_GetPresentPWM(self.dev, id,  nowforce)
            if id == 1 or id == 4:
                nowforce.value = nowforce.value * -1
            nowforces.append(nowforce.value)
        return nowforces
    
    def get_present_angles(self): #スタートとの角度の差を計算
        # self.start_angles = (ctypes.c_double * len(self.IDs))()
        # dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.start_angles, len(self.IDs)) 
        # print('(', end='')
        # print(('{:7.1f},'*len(self.start_angles)).format(*self.start_angles), end=')\n')  
        # self.move(1, -10)
        # self.move(2, -10)
        # self.move(3, -10)
        # self.move(4, -10)    
        # dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.start_angles, len(self.IDs)) 
        # print('(', end='')
        # print(('{:7.1f},'*len(self.start_angles)).format(*self.start_angles), end=')\n')  
        now_angles = (ctypes.c_double * len(self.IDs))()
        now_angles_list = []
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, now_angles, len(self.IDs))
        if self.start_angles == None:
            raise SyntaxError("Do back to initial potiosn")
        for id in self.IDs:
            angle = now_angles[id-1] - self.start_angles[id-1]
            if id == 1 or id == 4:
                angle = angle * -1
            now_angles_list.append(angle)
        return now_angles_list
        


    def move(self, id, angle_displacement):
        idi = id - 1
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.rotation_angles, len(self.IDs))
        gole_angles = self.rotation_angles

        #方向の調整
        if id ==  1 or id == 4:
            setangle = angle_displacement * -1
        else:
            setangle = angle_displacement

        gole_angles[idi] = gole_angles[idi] + setangle
        dx2.DXL_SetGoalAngles (self.dev, self.IDs,  gole_angles, len(self.IDs))
        dx2.DXL_GetPresentAngles(self.dev, self.IDs, self.rotation_angles, len(self.IDs))




    def manual_move(self, record = False):
        key = ''
        kb = kbhit.KBHit()
        while key != 'p':   # 'p'が押されると終了  
            if kb.kbhit():
                key = kb.getch()
        # ' '(スペース)を押す度にトルクイネーブルをトグル
                if key =='q':  
                    self.move(1, 10)
                if key =='w':  
                    self.move(2, 10)
                if key =='e':  
                    self.move(3, 10)
                if key =='r':  
                    self.move(4, 10)
                if key =='a':  
                    self.move(1, -10)
                if key =='s':  
                    self.move(2, -10)
                if key =='d':  
                    self.move(3, -10)
                if key =='f':  
                    self.move(4, -10)
                if record == True:
                    self.record_angle()
                print(self.get_present_angles())
                

                       

    def printAngle(self):

        print('(', end='')
        print(('{:7.1f},'*len(self.rotation_angles)).format(*self.rotation_angles), end=')\n')
    
    def record_angle(self, angles = []):
        now_angle = self.get_present_angles()
        now_time  = datetime.datetime.now()
        now_angle.insert(0, now_time)
        self.anglerecord.append(now_angle)



    # def measurement_rotation_angle():

    # def measurement_force():

# Motors = MyDynamixel()
# Motors.manual_move()
# Motors.back_to_initial_position()
# Motors.manual_move(record=True)


# print(Motors.anglerecord)
# with open('C:\\Users\\shigf\\Program\\DXhub\\data\\nosensor.csv', 'w',newline="") as f:
#     writer = csv.writer(f)
#     writer.writerows(Motors.anglerecord)

# Motors.manual_move()
# forces = Motors.get_present_PWMs()
# print(forces)
# Motors.back_to_initial_position()
# angles = Motors.get_present_angles()
# print(angles)
