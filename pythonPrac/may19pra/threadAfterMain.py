import time
import threading
def sing():
    for i in range(10):
        print("sing ",i)
        time.sleep(0.5)

def dance():
    for i in range(10):
        print("dance ",i)
        time.sleep(0.5)
    
if __name__ == '__main__':
    t1 = threading.Thread(target=sing)
    t1.daemon = True #子线程设置为守护线程
    t1.start()

    t2 = threading.Thread(target=dance)
    t2.daemon = True
    t2.start()
# 所有子线程都设置为True，才有用，只设置一个，线程都不会停
    time.sleep(2)
    print("--------------------------------")
    exit(0)