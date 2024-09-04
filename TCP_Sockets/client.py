# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 22:22:39 2024

@author: Sanjay Parmar
"""

import socket

c= socket.socket()

c.connect(('192.168.191.124',9999))

msg=c.recv(1024)
print(msg.decode())