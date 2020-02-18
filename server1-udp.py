# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:12:40 2020

@author: Davis Chan
"""

import socket
import subprocess
import threading
import time

terminate = 1
minNum = 0
maxNum = 0
aveNum = 0
lostNum = 0
port_number = 5555
#IP make sure to change
server_ip = '127.0.0.1'

def startPing():
    global terminate
    global minNum
    global maxNum 
    global aveNum 
    global lostNum
    temp = 0
    while terminate%2 == 0:
        out = subprocess.run(['ping', msg], capture_output=True)
        updated = out.stdout.decode()
        Min = updated.find('Minimum') 
        Max = updated.find('Maximum') 
        Ave = updated.find('Average') 
        Lost= updated.find('Lost')
        print(updated)
        Min = Min + 10
        Max = Max + 10
        Ave = Ave + 10
        Lost = Lost +7
        tempMinNum = int(updated[Min])
        tempMaxNum = int(updated[Max])
        tempAveNum = int(updated[Ave])
        tempLostNum = int(updated[Lost])
        if updated[Min+1].isnumeric() == True:
            tempMinNum = (int(tempMinNum)*10) + int(updated[Min+1])
            if updated[Min+2].isnumeric() == True:
                tempMinNum = (int(tempMinNum*10)) + int(updated[Min+2])
        if updated[Max+1].isnumeric() == True:
            tempMaxNum = (int(tempMaxNum*10)) + int(updated[Max+1])
            if updated[Max+2].isnumeric() == True:
                tempMaxNum = (int(tempMaxNum*10)) + int(updated[Max+2])
        if updated[Ave+1].isnumeric() == True:
            tempAveNum = (int(tempAveNum*10)) + int(updated[Ave+1])
            if updated[Ave+2].isnumeric() == True:
                tempAveNum = (int(tempAveNum*10)) + int(updated[Ave+2])
        if tempMinNum < minNum or minNum == 0:    
            minNum = tempMinNum
        if tempMaxNum > maxNum or maxNum == 0:
            maxNum = tempMaxNum
        if  aveNum == 0:
            aveNum = tempAveNum
        else:
            aveNum = (aveNum + tempAveNum)/2
        lostNum = int(lostNum) + int(tempLostNum)
        print(minNum)
        print(maxNum)
        print(aveNum)
        print(lostNum)

def sendPing():
    global terminate
    global minNum
    global maxNum 
    global aveNum 
    global lostNum
    while terminate%2 == 0:
        time.sleep(5)
        message = ("Min: {} Max: {} Ave: {} Lost: {}".format(minNum,maxNum,aveNum,lostNum))
        s.sendto( message.encode('ascii'), (addr))
        
    
        
def endPing():
    global terminate
    terminate +=1


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind( (server_ip, port_number))

while True:
    (msg, addr) = s.recvfrom(1024)
    msg = msg.decode('ascii')
    if msg == 'end':
        a = threading.Thread(target=endPing)
        a.start()
    elif msg == 'die':
        break
    else:
        b = threading.Thread(target=startPing)
        c = threading.Thread(target=sendPing)
        terminate +=1
        b.start()
        c.start()
        



        
