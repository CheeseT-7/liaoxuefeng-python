#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 21:17
# @Author  : TQS
# @File    : udp_client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'a', b'b', b'c']:
    s.sendto(data, ('127.0.0.1', 9998))
    print(s.recv(1024).decode('utf-8'))

s.close()
