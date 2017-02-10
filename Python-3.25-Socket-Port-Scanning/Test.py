import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = input('What website to scan ? : ')

def portScanner(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False


for x in range(1, 27):
    if portScanner(x):
        print("Post ",x," is open")
    else:
        print("Post ", x, " is close")

