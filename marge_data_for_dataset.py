import pickle
import numpy as np
from myclass import myfunction
import datetime, os, csv

with open('magsensor20241202_205921.pickle', mode='br') as fi:
  magsensor = pickle.load(fi)

with open('motor20241202_205921.pickle', mode='br') as fi:
  motordata = pickle.load(fi)

with open('motioncapture20241202_205921.pickle', mode='br') as fi:
  motiondata = pickle.load(fi)
  
  
def mag_data_change(row):
    row = delete_date(row)
    if row[0] == '':
        return []
    split_value = row[0].split('/')
    return split_value


def delete_date(row):
    copyrow = row.copy()
    copyrow.pop(0)
    return copyrow

margedata = []





for motionrow in motiondata:
    one_dataset = []


    for motorrow in motordata:
        if motorrow[0] > motionrow[0]:
            afterdiff = motorrow[0] - motionrow[0]
            beforediff =motionrow[0] - temprow[0]
            if afterdiff < beforediff:
                motorrow = delete_date(motorrow)
                one_dataset.extend(motorrow)
            else:
                temprow = delete_date(temprow)
                one_dataset.extend(temprow)
            break
        temprow = motorrow
    for magrow in magsensor:
        if magrow[0] > motionrow[0]:
            afterdiff = magrow[0] - motionrow[0]
            beforediff = motionrow[0] - temprow[0]
            if afterdiff < beforediff:
                magrow = mag_data_change(magrow)
                one_dataset.extend(magrow)
            else:
                temprow = mag_data_change(temprow)
                one_dataset.extend(temprow)
            break
        temprow = magrow
        
    one_dataset.insert(0,motionrow[0])
    motionrow = delete_date(motionrow)
    one_dataset.extend(motionrow)
    
    margedata.append(one_dataset)

print(margedata)
margedata.insert(0, ["time","rotate1","rotate2","rotate3","rotate4","force1","force2","force3","force4","sensor1","sensor2","sensor3","sensor4","sensor5","sensor6","sensor7","sensor8","sensor9","Mc1x","Mc1y","Mc1z","Mc2x","Mc2y","Mc2z","Mc3x","Mc3y","Mc3z","Mc4x","Mc4y","Mc4z","Mc5x","Mc5y","Mc5z"])



myfunction.wirte_csv( margedata, filename = "margedata")

