from socket import *
import utils

udp_socket = socket(AF_INET, SOCK_DGRAM)
udp_socket.bind(("",8882))
print("udf receiving----------------")

result_data, addr = udp_socket.recvfrom(1024)
print(utils.decode_data(result_data))

udp_socket.close()