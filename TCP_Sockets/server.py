# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 21:54:52 2024

@author: Sanjay Parmar
"""

import socket
#.socket() takes two args one ipv4(AF_INET) or ipv6(AF_INET6) and second is tcp(SOCK_STREAM)/
#udp(SOCK_DGRAM) if not passing default will be v4 and tcp.
s = socket.socket()
print('Socket Created.')

#Accepting coonection using binding it takes two args ip address and port number.
#ports=0 to 65535.
s.bind(('192.168.191.124',9999))

#connects client
s.listen(3)
print('Waiting for connections...')

while True:
#it gives client socket and address     
    c, addr=s.accept()
    print('Connected with', addr) 
    
    c.send('Welcome...'.encode('utf-8'))
    c.close()


