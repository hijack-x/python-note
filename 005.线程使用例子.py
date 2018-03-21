#!/bin/python3

# -*- coding: utf-8 -*-

import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print('thread begin: ', self.name)
        time.sleep(random.randint(1, 3)) # sleep a random time
        print('thread end: ', self.name)


thread1 = MyThread('Thread-1')
thread2 = MyThread('Thread-2')

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print('main thread exit')
