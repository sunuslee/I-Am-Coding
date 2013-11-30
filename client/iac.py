#!/usr/bin/env python
# encoding=utf-8

import socket
import simplejson as json
from iac_config import iac_config
from diff_match_patch import diff_match_patch


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

    old_text = ''
    new_text = ''

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(backlog)

    while True:
        client, address = s.accept()
        data = client.recv(size)
        if data:
            data = data.split('\r\n\r\n')[1]
            new_text = data.split('\n', 1)[1]
            print 'new text\n', new_text
            send_diff2server(old_text, new_text)
            old_text = new_text
        client.close()


def send_diff2server(old_text, new_text):

    """Generate diffs of how old_text become new_text"""

    dmp = diff_match_patch()
    diffs = dmp.diff_main(new_text, old_text)
    print json.dumps(diffs, indent='  ')

if __name__ == '__main__':
    main()
