import os

file_name= None

while True:
    file_name=input("请输入文件名：")
    if os.path.exists(file_name):
        break
    print("文件不存在，请重新输入！")
    
dot_index = file_name.rindex(".")
pre_name = file_name[:dot_index]
after_name = file_name[dot_index:]
print(pre_name,after_name)

new_file_name = pre_name+"[copy]"+after_name
with open(file_name,'r',encoding='utf-8') as f:
    content = f.read()
    with open(new_file_name,'w',encoding='utf8') as new_f:
        new_f.write(content)