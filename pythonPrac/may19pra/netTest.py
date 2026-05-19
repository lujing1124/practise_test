import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("127.0.0.1",7788))
tcp_server.listen(10)

client,addr = tcp_server.accept()
print("client's message:",client.recv(1024).decode("GBK"))
tcp_server.close()