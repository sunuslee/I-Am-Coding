#!/usr/bin/env python
# encoding=utf-8

"""
A Simple Socker Server
to test if editor's plugins  working properly
"""

import socket

host = ''
port = 7375
backlog = 5
size = 4096
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)
while True:
    client, address = s.accept()
    data = client.recv(size)
    if data:
        print 'Got data:'
        print data
    client.close()
