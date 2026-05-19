import socket
import threading
from utils import decode_data 

def handle_client(client_tcp : socket.socket,client_addr):
    client_tcp.send("welcome to our house")
    while True:
        bytes_data = client_tcp.recv(2048)
        if bytes_data :               
            msg = decode_data(bytes_data)
            print(msg)
        else:
            client_tcp.close()
            print(f"{client_addr} leaved")
            break

if __name__ == '__main__':
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("",8888))
    tcp_server_socket.listen(128)
    print("server start.....")
    while True:
        client_tcp, client_addr = tcp_server_socket.accept()
        thread = threading.Thread(target=handle_client, args=(client_tcp,client_addr))
        thread.daemon = True
        thread.start()
        
        
        
    