# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 14:02:37 2018

@author: APL14
"""

import csv

plMargin = 0.40
profit = 30
cumulateLoss = 0.0
value=0.0
quantity=0.0
with open("1.csv", "r") as f:
    reader = csv.reader(f)
    headerList = next(reader)
    index = headerList.index(str(plMargin))
    profitList = [float(row[index]) for row in reader]

with open("2.csv", "r") as f:
    reader = csv.reader(f)
    headerList = next(reader)
    index = headerList.index(str(plMargin))
    lossList = [float(row[index]) for row in reader]

def recursiveCalculate(value):
    if((value+profit)> profitList[len(profitList)-1]):
        return
    for i in range(len(profitList)):
        if(profitList[i]>(value+profit)):
            value = value -lossList[i]
            print("Quantity: " + str(i+1) + "\tP: " + str(profitList[i]) + "\tL: " + str(lossList[i]) + "\tCL: " + str(value))
            break
    recursiveCalculate(value)
    return
            

for i in range(len(profitList)):
    if(profitList[i]>profit):
        value = profitList[i]
        quantity = i+1
        loss = lossList[i]
        cumulateLoss = cumulateLoss+loss
        break

print("Quantity: " + str(quantity) + "\tP: " + str(value) + "\tL: " + str(loss) + "\tCL: " + str(0-cumulateLoss))
cumulateLoss = 0-cumulateLoss
recursiveCalculate(cumulateLoss)