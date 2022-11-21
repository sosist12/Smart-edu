import socket

id_addr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
id_addr.connect(("www.google.co.kr",443))
print(id_addr.getsockname()[0])