# coding=utf-8
import threading

import time

'''
Python多线程使用
'''


class MutilThreads():

    def threads(self, num):
        print('%s this thread is starting:' % threading.current_thread().name)
        for i in range(num):
            time.sleep(1)
            print('%s:%d' % (threading.current_thread().name, i))
        print('%s this thread is stopping!' % threading.current_thread().name)


t = MutilThreads()

print("%s start" % threading.current_thread().name)
t1 = threading.Thread(target=t.threads, args=(6,))
t2 = threading.Thread(target=t.threads, args=(11,))
t1.start()
t1.join()

t2.start()
t2.join()
print("%s stop" % threading.current_thread().name)
