import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection = s.connect(("https://google.com",80))
if not connection:
    print(port)