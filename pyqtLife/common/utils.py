import socket
def get_local_ip():
    local_ips = ["127.0.0.1"]
    for ip in socket.gethostbyname_ex(socket.gethostname())[2]:
        local_ips.append(ip)

    local_ips.sort(reverse=True)
    return local_ips

def decode_data(bytes_arr: bytes) -> str:
    try:
        msg = bytes_arr.decode("utf8")
    except Exception as e:
        msg = bytes_arr.decode("GBK")

    return msg

# if __name__ == '__main__':
#     print(get_local_ip())