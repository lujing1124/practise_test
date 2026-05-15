# f=open("a.txt",encoding="utf-8")
# content = f.read()
# print(content)
# f.close() 

# f=open("a.txt",encoding="utf-8")
# # content = f.read(5)
# # content = f.readline()
# content = f.readlines()
# print(content)
# f.close() 

# f=open("b.txt","w",encoding="utf-8")
# f.write('哈哈哈，您好哦')
# f.close()


# f=open("c.txt","w",encoding="utf-8")
# list = ['今天天气不错','我们要学习']
# list = [item+'\n' for item in list]
# f.writelines(list)
# f.close()


# with open("d.txt","w",encoding="utf-8") as f:
#     list = ['今天天气不错','我们要学习','还有爱你哦！',"朝朝暮暮"]
#     content = "\n".join(list)
#     f.writelines(content)
# print("closed:",f.closed)

with open("../myUtil.py",encoding="utf-8") as f:
    print(f.read())
print("closed:",f.closed)