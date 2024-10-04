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

    
    
    
def dlrandom():
    datas = []
    motor_max = 300
    motor_angle = np.array([150, 150, 150, 150])
    dlmax = 5
    trial_num = 10
    cos_similarity = 0
    i = 0
    while i < trial_num:
        change_i = random.randrange(4)
        change_range = random.uniform(-4, 4)
        if motor_angle[change_i] + change_range < motor_max and motor_angle[change_i] + change_range > 0:
            motor_angle[change_i] = motor_angle[change_i] + change_range
            datas.append(motor_angle)  
            i = i + 1
    return datas

def lrandom():
    datas = []
    motor_max = 300
    dlmax = 5
    trial_num = 10
    cos_similarity = 0
    i = 0
    start_angle = np.array([0,0,0,0])
    while(True):
        goal_angle = np.random.rand(4) * 300
        
        for j in l2:
            print(i, j)
            if i == 2 and j == 20:
                print('BREAK')
                break
        else:
            continue
        break
        

def complement_between(a,b):
    anglelist = []
    max_change = 5
    angle = a
    pm = (b - a) / abs(b-a)
    while angle < b:
        change_range = random.uniform(1, 4)
        angle = angle + change_range * pm
        anglelist.append(angle)
    return angle
    





data = dlrandom()
sim = culc_similarity(data)
print(sim)

