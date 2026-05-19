# import time
# def sing():
#     for i in range(5):
#         print("sing ",i)
#         time.sleep(1)

# def dance():
#     for i in range(5):
#         print("dance ",i)
#         time.sleep(1)
    
# if __name__ == '__main__':
#     sing()
#     dance()

import time
import threading
def sing(name,age,score):
    for i in range(5):
        print(f"{name} is {age} sing: score is {score}",i)
        time.sleep(0.5)

def dance(name,age=20,score=0):
    for i in range(5):
        print(f"{name} is {age} dance: score is {score}",i)
        time.sleep(1)
    
if __name__ == '__main__':

    t2 = threading.Thread(target=dance,args=("chuan",))#最后一定要加逗号，
    t1 = threading.Thread(target=sing,kwargs={"name":"jenny","age":13,"score":40})
    t1.start()
    t2.start()