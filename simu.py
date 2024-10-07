import random

import numpy as np

def cos_sim(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def culc_similarity(datas):
    motor_angle_base = np.array([150, 150, 150, 150])
    sim = 0
    for v1 in datas:
        sim = sim + cos_sim(motor_angle_base, v1)
    sim = sim / len(datas)
    return sim

    
    
# 変位幅をランダムで与える手法
def dlrandom():
    datas = []
    motor_max = 300
    motor_angle = np.array([150, 150, 150, 150])
    trial_num = 10
    i = 0
    while i < trial_num:
        change_i = random.randrange(4)
        change_range = random.uniform(-4, 4)
        if motor_angle[change_i] + change_range < motor_max and motor_angle[change_i] + change_range > 0:
            motor_angle[change_i] = motor_angle[change_i] + change_range

            #動かしたりの処理

            datas.append(motor_angle)  
            i = i + 1
    return datas

#ランダムに決めた値にランダムな幅で進んでいく手法
def lrandom():
    datas = []
    motor_max = 300
    trial_num = 10
    i = 0
    start_angle = np.array([0,0,0,0])
    goal_angle = np.random.rand(4) * motor_max
    changestep =  [[] for _ in range(4)]
    for anglenum in range(4):
        changestep[anglenum] = complement_between(start_angle[anglenum], goal_angle[anglenum])
    changestep_list = [0,1,2,3] #changestepがおわってるか
    while(True):
        while changestep_list != []:
            for changestep_num in changestep_list:
                if changestep[changestep_num] == []:
                    changestep_list.remove(changestep_num)
                else:
                    if i > trial_num:
                        break 
                    start_angle[changestep_num] = changestep[changestep_num].pop(0)
                    datas.append(start_angle.copy())
                    i = i + 1
            else:
                continue
            break
        else:
            continue
        break
        
    return datas
 
        
#目的地を与えるとランダムに進んでいく幅を決める関数
def complement_between(a,b):
    anglelist = []
    max_change = 5
    angle = a
    if a == b:
        return [b]
    pm = (b - a) / abs(b-a)
    while pm * angle <  pm * b:
        change_range = random.uniform(1, 4)
        angle = angle + change_range * pm
        if angle * pm < pm * b:
            anglelist.append(angle)
    anglelist.append(b)
    return anglelist
    
def lrandom():
    datas = []
    motor_max = 300
    trial_num = 10
    i = 0
    start_angle = np.array([0,0,0,0])
    goal_angle = np.random.rand(4) * motor_max
    changestep =  [[] for _ in range(4)]
    for anglenum in range(4):
        changestep[anglenum] = complement_between(start_angle[anglenum], goal_angle[anglenum])
    changestep_list = [0,1,2,3] #changestepがおわってるか
    while(True):
        while changestep_list != []:
            for changestep_num in changestep_list:
                if changestep[changestep_num] == []:
                    changestep_list.remove(changestep_num)
                else:
                    if i > trial_num:
                        break 
                    start_angle[changestep_num] = changestep[changestep_num].pop(0)
                    datas.append(start_angle.copy())
                    i = i + 1
            else:
                continue
            break
        else:
            continue
        break
        
    return datas
 

def lfix_bet_randam():
    datas = []
    i = 0
    start_angle = np.array([0,0,0,0])
    angle = np.array([0,0,0,0])
    goal_anglelist = np.array([[300,0,0,0],[0,300,0,0],[0,0,300,0],[0,0,0,300],\
                              [300,300,0,0],[300,0,300,0],[300,0,0,300],[0,300,300,0],[0,300,0,300],[0,0,300,300],\
                              [0,300,300,300],[300,0,300,300],[300,300,0,300],[300,300,300,0],[300,300,300,300]])
    
    for num in range(len(goal_anglelist)):
        changestep =  [[] for _ in range(4)]
        for anglenum in range(4):
            changestep[anglenum] = complement_between(angle[anglenum], goal_anglelist[num][anglenum])
        changestep_list = [0,1,2,3] #changestepがおわってるか
        while changestep_list != []:
            for changestep_num in changestep_list:
                if changestep[changestep_num] == []:
                    changestep_list.remove(changestep_num)
                else:
                    angle[changestep_num] = changestep[changestep_num].pop(0)
                    datas.append(angle.copy())
                    i = i + 1

        changestep =  [[] for _ in range(4)]
        for anglenum in range(4):
            changestep[anglenum] = complement_between(angle[anglenum],start_angle[anglenum])
        changestep_list = [0,1,2,3] #changestepがおわってるか
        while changestep_list != []:
            for changestep_num in changestep_list:
                if changestep[changestep_num] == []:
                    changestep_list.remove(changestep_num)
                else:
                    angle[changestep_num] = changestep[changestep_num].pop(0)
                    datas.append(angle.copy())
                    i = i + 1
    
    print(i)
    return datas
 


data = lfix_bet_randam()

print(data)
