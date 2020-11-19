import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = "GET http://data.pr4e.org/romeo.txt HTTP/1.0 /n/n".encode()
mysock.send(cmd)

while True:
    print("downloading data...")
    data = mysock.recv(512)
    if len(data) < 1:
        print("finished")
        break
    print(data.decode())
mysock.close()

