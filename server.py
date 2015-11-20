#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket as SocketService
import sys
from thread import * 

# 設定
HOST    = '0.0.0.0' # 接收所有連線
PORT    = 13128
MAX_CLI = 5
TIMEOUT = 10

# 處理多執行緒的子程式
def threadWork(client):
    
    while True:
        
        # 接收客戶端訊息
        msg = client.recv(1024)
        
        if not msg:
            pass
        else:
            
            print "Client send: " + msg
            resp = "Hello :) You send: " + msg + "\r\n"
            
            # 回應客戶端
            print "Respond: " + resp
            client.send(resp)
            
            client.close()
            return # 結束子程式

# ------------------------

try:
    
    # 建立 Socket 物件
    sock = SocketService.socket(
        SocketService.AF_INET,     # 接受外網連線
        SocketService.SOCK_STREAM  # TCP
    )

except SocketService.error, msg:
    
    # 錯誤處理
    sys.stderr.write("[ERROR] %s\n" % msg[1])
    sys.exit(1)

# 允許 TCP Handle 被重複使用
sock.setsockopt(SocketService.SOL_SOCKET, SocketService.SO_REUSEADDR, 1) 

# 綁定傾聽 IP 和 Port
sock.bind((HOST, PORT))
sock.listen(MAX_CLI)


print 'Server listening on tcp://' + HOST + ':' + str(PORT) + "\n"

# Keep Listen
count = 1

while True:
    
    (clientsocket, address) = sock.accept()
    print "Client connected:", address
    print "Connect counter: ", count

    # 啟動子程序
    start_new_thread(threadWork, (clientsocket, ))
    count += 1

sock.close()

