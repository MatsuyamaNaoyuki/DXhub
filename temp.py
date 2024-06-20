#位置制御を行うが，トルクを測定し，そこまでみたいなのを試す

import sys, time
import ctypes
from package import kbhit
from package import dx2lib as dx2
from package import setting
def change_torque(dev, IDs, id, new_torque):
    for i in range(len(IDs)):
        if IDs[i] == id:
            id_subscript = i
    print(id_subscript)
    now_torque = (ctypes.c_double)()
    now_angle = (ctypes.c_double)()
    dx2.DXL_GetPresentPWM(dev, id, now_torque)
    while(abs(new_torque - abs(now_torque.value)) > 1):
        dx2.DXL_GetPresentAngle(dev, id, now_angle)
        if new_torque - abs(now_torque.value) > 0:
            if id == 1 or 4:
                new_angle = now_angle.value - 1 
            else:
                new_angle = now_angle.value + 1
        else:
            if id == 1 or 4:
                new_angle = now_angle.value + 1 
            else:
                new_angle = now_angle.value - 1
        dx2.DXL_GetPresentPWM(dev, id, now_torque)
        


          
    



  

# ID一覧
IDs = (ctypes.c_uint8 * 4)(1,2,3,4)

change_torque(IDs, 4, 1)



