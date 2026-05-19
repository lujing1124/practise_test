from socket import *

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("",3333))
addr = ("127.0.0.1",8888)
data = "你好".encode("utf8")


udp_socket.sendto(data, addr)
udp_socket.close()