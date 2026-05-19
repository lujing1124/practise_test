import socket

tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
addr = ("127.0.0.1",8080)#服务器ip，端口
tcp_client_socket.connect(addr)
tcp_client_socket.send("你好".encode())
data = tcp_client_socket.recv(2048)
print(data.decode('GBK'))
tcp_client_socket.close()

#回家些代码积极性还是差了点，写到11点，我就不想写了，每天刷3小时课程，两天刷老师的一天课程
# 其实周末在家，效果还差点，平时上班，下了班反而有点积极性
# 我想要是晚一点被离职就好了
# 大概还有10天左右吧，十分焦虑。