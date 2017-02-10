import threading
import time

tLock = threading.Lock()


class MyThread:
    def timer(self, name, delay, repeat):
        tLock.acquire()
        print("Timer started")
        while repeat > 0:
            time.sleep(delay)
            print(name, " : ", str(time.ctime(time.time())))
            repeat -= 1
        print(name, " stop")
        tLock.release()


def Main():
    obj = MyThread()
    t1 = threading.Thread(target=obj.timer, args=("Timer 1", 1, 5))
    t2 = threading.Thread(target=obj.timer, args=("Timer 2", 1, 5))
    t1.start()
    t2.start()


if __name__ == "__main__":
    Main()

