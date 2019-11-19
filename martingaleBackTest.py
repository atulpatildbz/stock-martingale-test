# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 10:31:31 2019

@author: APL14
"""

import requests
from datetime import datetime, timezone
# print(datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S'))

#dd/mm/yyyy
fromstrTime = "11/10/2018"
tostrTime = "07/11/2019"
candle = "60"
symbol = "946660"
percent = 65


fromTime = str(int(datetime.strptime(fromstrTime, "%d/%m/%Y").timestamp()))
toTime = str(int(datetime.strptime(tostrTime, "%d/%m/%Y").timestamp()))


f = open("log.txt", "w")

url = "https://tvc4.forexpros.com/968ffe4eac175bb867cc58f1ee375dbc/1551413467/56/56/23/history?"+"symbol="+symbol+"&"+"resolution="+candle+"&"+"from="+fromTime+"&"+"to="+toTime
#url = "https://tvc4.forexpros.com/968ffe4eac175bb867cc58f1ee375dbc/1551413467/56/56/23/history?symbol=947233&resolution=D&from=1497157552&to=1551416853"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
resp = requests.get(url=url, headers=headers)
data = resp.json()

closeArray = data.get('c')
timeArray = data.get('t')

price = round(closeArray[0],2)

initialInv = 10000


buysArray = []
exitsArray = []
# invAmountArray = [initialInv]
up = 1+(1*percent/100)
down = 1-(1*percent/100)

def buyExitCalc(price):
    global buysArray, exitsArray, initialInv
    buysArray = []
    exitsArray = []
    buysArray.append(round(price,2))
    exitsArray.append(round(price*up,2))
    for i in range(2,15):
        price = down*price
        # initialInv = initialInv*2
        buysArray.append(round(price,2))
        exitsArray.append(round(price*up,2))
        # invAmountArray.append(initialInv)


buyExitCalc(price)

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
def aslocaltimestr(utc_dt):
    return utc_to_local(utc_dt).strftime('%Y-%m-%d %H:%M:%S')


buyNumber = 1

f.write("Buy number: "+str(buyNumber)+"\tat: "+ str('{0:.2f}'.format(round(price,2))))
f.write("\ttime: "+aslocaltimestr(datetime.utcfromtimestamp(timeArray[0])))
f.write("\tAmount: "+str(initialInv*(pow(2,(buyNumber-1)))))
f.write("\n")

lastBuy = price

print("Buy number: "+str(buyNumber)+" at "+ str(price))
completedCounter = 0
for idx, val in enumerate(closeArray):
    if(val >= exitsArray[buyNumber-1]):
        completedCounter = completedCounter+1
        f.write('completed : ' + str(completedCounter))
        f.write("\texit: "+str(round(val)))
        f.write("\ttime: "+aslocaltimestr(datetime.utcfromtimestamp(timeArray[idx])))
        f.write("\tpercent: "+str(round(((val-lastBuy)/lastBuy)*100,2))+"\n")
        f.write('-----------------------------------\n')
        print('completed : ' + str(completedCounter) + " exit at: " + str('{0:.2f}'.format(val)))
        if(idx+1 >= len(closeArray)):
            break
        buyExitCalc(closeArray[idx+1])
        f.write("NEW buy at: " + str('{0:.2f}'.format(closeArray[idx+1])))
        f.write("\ttime: "+aslocaltimestr(datetime.utcfromtimestamp(timeArray[idx+1]))+"\n")
        print("NEW buy at: " + str('{0:.2f}'.format(closeArray[idx+1])))
        lastBuy = closeArray[idx+1]
        buyNumber=1
        # break
    if(val <= buysArray[buyNumber]):
        buyNumber = buyNumber+1
        f.write("Buy Number: " + str(buyNumber) +"\tat: "+str('{0:.2f}'.format(round(val,2))))
        f.write("\ttime: "+aslocaltimestr(datetime.utcfromtimestamp(timeArray[idx])))
        f.write("\tAmount: "+str(initialInv*(pow(2,(buyNumber-1)))))
        f.write("\tpercent: "+str(round(((val-lastBuy)/lastBuy)*100,2))+"\n")
        lastBuy = val
        print("Buy Number: " + str(buyNumber) +" at: "+str('{0:.2f}'.format(val)))


f.close()