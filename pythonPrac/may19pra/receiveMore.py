import socket

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server.bind(("127.0.0.1",7788))
tcp_server.listen(10)
print("----------recv---------------")
while True:
    client,addr = tcp_server.accept()
    print("client :",addr)
    while True:
        client_data = client.recv(1024)
        if client_data:
            print("client's message:",client_data.decode("GBK"))
            client.send("message received!\n".encode())
        else:
            print(f"client {addr} leave")
            client.close()
            break


tcp_server.close()