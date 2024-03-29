#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/2/15 20:46
# @Author  : TQS
# @File    : tcp_client.py

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
#
# s.send(b'GET / HTTP/1.1'
#        b'HOST:www.sina.com.cn'
#        b'Connection:close'
#        b''
#        b'')
#
# buffer = []
# while True:
#     d = s.recv(1024)
#     if d:
#         buffer.append(d)
#     else:
#         break
# data = b''.join(buffer)
#
# s.close()
#
# header, body = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))
# with open('sina.html', 'wb') as f:
#     f.write(body)

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8'))
for data in [b'A', b'B', b'c']:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()
