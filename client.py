#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket as SocketService
import sys

HOST    = sys.argv[1]
PORT    = int(sys.argv[2])

try:
    sock = SocketService.socket(SocketService.AF_INET, SocketService.SOCK_STREAM)
except SocketService.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)
 
try:
    print "Trying to connect to " + HOST + ':' + str(PORT)
    sock.connect((HOST, PORT))
except SocketService.error, msg:
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    exit(1)
 
sock.send("Hello I'm Client.")
print "--- Server Respond Below ---"
print sock.recv(1024)
sock.close()