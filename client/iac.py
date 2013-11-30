#!/usr/bin/env python
# encoding=utf-8

import sys
import socket
from iac_config import iac_config

def login(username, password):
    return True

def main():
    username = iac_config['username']
    password = iac_config['password']
    host = ''
    port = iac_config['port']
    size = 8192
    backlog = 5

    if login(username, password) is not True:
        print "Can't login in right now."
        return -1
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))
    s.listen(backlog)
    old_text = ''
    new_text = ''
    while True:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            data = data.split('\r\n\r\n')[1]
            print 'Got data:'
            print data
        client.close()


if __name__ == '__main__':
    main()
