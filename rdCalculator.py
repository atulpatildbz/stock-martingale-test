# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 12:43:45 2018

@author: Atul
"""

#****************************
#buyQuantity = 1000
#sellQuantity = buyQuantity
#buyRate = 255
#sellRate = 255.30
#****************************

def getPL(buyRate, sellRate, buyQuantity, sellQuantity=0):
    if(sellQuantity==0):
        sellQuantity = buyQuantity
    brokerage = 0.00005
    buyAmount = buyQuantity * buyRate
    sellAmount = sellQuantity * sellRate

    tatDiff = sellAmount - buyAmount

    #deductions
    buyBrokerage = buyAmount * brokerage
    sellBrokerage = sellAmount * brokerage
    stt = 0.00025 * sellAmount
    serviceTaxTotal = (0.1236 * buyBrokerage) + (0.1236 * sellBrokerage)
    swatchBharatTotal = (0.0050 * buyBrokerage) + (0.005 * sellBrokerage)
    krushiKalyanTotal = swatchBharatTotal
    transTotal = (0.0000348 * buyAmount) + (0.0000348 * sellAmount)
    sebi = (0.0000011 * buyAmount) + (0.0000011 * sellAmount)
    stamp = (0.00002 * buyAmount) + (0.00002 * sellAmount)
    deductions = buyBrokerage + sellBrokerage + stt + serviceTaxTotal + swatchBharatTotal + krushiKalyanTotal + transTotal + sebi + stamp
    netPL = tatDiff - deductions

    return(netPL)
#**************************
#inupt values here
increment = 100
maxAmount = 2500
initial = 175
#**************************
f = open("1.csv", "w+")
f.write('Quantity,')
for j in range(1,increment):
        f.write(str(round(0.05*j,2)) +',')
f.write('\n')
for i in range(1,maxAmount):
    f.write(str(i)+',')
    for j in range(1,increment):
        f.write(str(round(getPL(initial,initial+(0.05*j),i),2)) +',')
    f.write('\n')

f.close()

f = open("2.csv", "w+")
f.write('Quantity,')
for j in range(1,increment):
        f.write(str(round(0.05*j,2)) +',')
f.write('\n')
for i in range(1,maxAmount):
    f.write(str(i)+',')
    for j in range(1,increment):
        f.write(str(round(getPL(initial,initial-(0.05*j),i),2)) +',')
    f.write('\n')

f.close()