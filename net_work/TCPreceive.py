import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("127.0.0.1",7788))

tcp_server.listen(6)
print("server open---------------------")
client,clientAddr = tcp_server.accept()
print("new client",client)
data = client.recv(1024)
print(data.decode("GBK"))

client.send("I received!".encode())
client.close()
tcp_server.close()
