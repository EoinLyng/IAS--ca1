'''
UDPClient1 by: Eoin Lyng
Assignment 1
Send UDP packets to a particular address and port.
Alpha: 12NOV23
'''

import socket
import time
from datetime import datetime
import settings.udp as settings
import random

UDP_IP = settings.UDP["SERVER_UDP_IPv4"]
UDP_PORT = settings.UDP["SERVER_PORT"]

print(f'This is the UDP client, it will try to connect to a server at {UDP_IP}:{UDP_PORT} in the settings file.')
print('This script has no error handling, by design')

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        #list include letters and numbers to simulate error log with random letter instead of integer
        temp_list = [-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,18,20,21,23,24,25,26,27,28,29,30,31,35,32,33,34,35,'a','b','c','d']
        #create random range between -5 and 35 degrees https://www.w3schools.com/python/ref_random_randrange.asp
        message_text = f"SensorOne,Degrees Temperature in Celsius,{(random.choice(temp_list))},{datetime.now()}"
        message = message_text.encode('utf-8')
        s.sendto(message, (UDP_IP, UDP_PORT))
        print(f'Sensor Temperature Reading - {message_text}')
        time.sleep(30)
