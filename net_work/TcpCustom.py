import socket

tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ("127.0.0.1",8080)#服务器ip，端口
tcp_client_socket.connect(addr)
tcp_client_socket.send("你好".encode())
tcp_client_socket.close()