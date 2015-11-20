# SimpleSocket.py

Simple Server &amp; Client Socket written in Python


## Server Usage

```
$ python server.py
Server listening on tcp://0.0.0.0:13128

Client connected: ('127.0.0.1', 64991)
Connect counter:  1
Client send: Hello I'm Client.
Respond: Hello :) You send: Hello I'm Client.
```

## Clinet Usage

```
$ python client.py 127.0.0.1 13128
Trying to connect to 127.0.0.1:13128
--- Server Respond Below ---
Hello :) You send: Hello I'm Client.
```