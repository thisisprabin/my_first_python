import socket
import threading

print_lock = threading.Lock()

server = "youtube.com"

def portScanner(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((server, port))
        with print_lock:
            print(port," is open")
        con.close()
    except:
        print(port, " is close")

for x in range(1, 101):
    t = threading.Thread(target=portScanner(x))
    t.start()
