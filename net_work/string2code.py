by_arr = "今晚吃鸡，大吉大利".encode()
by_arr1 = "今晚大吉大利".encode(encoding='utf-8')
by_arr2 = "吃鸡，大吉大利".encode(encoding='gbk')
print(by_arr1,type(by_arr))
print(by_arr2,type(by_arr))


print(by_arr1.decode(encoding='utf8'))
print(by_arr1.decode(encoding='gbk'))
print(by_arr2.decode(encoding='gbk'))