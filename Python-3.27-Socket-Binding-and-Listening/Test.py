import socket
import sys

host = ''
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except socket.error as e:
    print(str(e))

s.listen(5)
con, add = s.accept()

print("Connected to :"+add[0]+" : "+str(add[1]))
