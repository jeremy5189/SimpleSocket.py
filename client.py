#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket as SocketService
import sys

# Check for empty command line arguments
if len(sys.argv) < 3:
	print 'Usage:   python client.py [host] [port]'
	print 'Example: python client.py 127.0.0.1 13128'
	exit(0)

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
