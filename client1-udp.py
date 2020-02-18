# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 10:12:40 2020

@author: Davis Chan
"""


import socket
import threading


loop = 0
port_number = 5555
server_ip = '127.0.0.1'

def send():
    global loop 
    global port_number
    global server_ip
    while loop == 0:
        message = input("What do you want to send?")
        s.sendto( message.encode('ascii'), (server_ip, port_number))
        if message == 'die':
            loop = 1
        
    
def recieve():
    global loop
    while loop == 0:
        (msg, addr) = s.recvfrom(1024)
        msg = msg.decode('ascii')
        print("{}".format(msg))

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#while loop == 0:
message = input("What do you want to send?")
s.sendto( message.encode('ascii'), (server_ip, port_number))
if message == 'die':
        loop = 1


#a = threading.Thread(target=send)
#a.start()
b = threading.Thread(target=recieve)
b.start()

while loop == 0:
    message = input("What do you want to send?")
    s.sendto( message.encode('ascii'), (server_ip, port_number))
    if message == 'die':
        loop = 1
