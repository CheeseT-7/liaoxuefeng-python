#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 21:17
# @Author  : TQS
# @File    : udp_server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 9998))

print('Bind UDP on 9998')
while True:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s' % addr)
    s.sendto(b'Hello, %s ' % data, addr)

