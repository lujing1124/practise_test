def decode_data(byte_arr: bytes):
    try:
        msg = byte_arr.decode("utf8")
    except Exception as e:
        msg = byte_arr.decode("GBK")

    return msg