from socket import *

# udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.setsockopt(SOL_SOCKET, SO_BROADCAST, True)

udp_socket.bind(("", 3333))
data = "来村东头老王家吃喜酒！".encode("UTF-8")
addr = ("192.168.10.255", 8888)

udp_socket.sendto(data, addr)
print("send")
udp_socket.close()