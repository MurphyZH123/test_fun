import threading
import time


class Test01(threading.Thread):
    def run(self):
        while True:
            if max01.acquire():
                print('1111')
                time.sleep(1)
                max02.release()


class Test02(threading.Thread):
    def run(self):
        while True:
            if max02.acquire():
                print('2222')
                time.sleep(1)
                max03.release()


class Test03(threading.Thread):
    def run(self):
        while True:
            if max03.acquire():
                print('3333')
                time.sleep(1)
                max01.release()


if __name__ == '__main__':
    max01 = threading.Lock()
    max02 = threading.Lock()
    max02.acquire()
    max03 = threading.Lock()
    max03.acquire()
    t01 = Test01()
    t02 = Test02()
    t03 = Test03()
    t01.start()
    t02.start()
    t03.start()














