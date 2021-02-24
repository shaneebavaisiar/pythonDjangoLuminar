from threading import *
import time

class Myclass:
    def job(self):
        for i in range(10):
            time.sleep(2)
            print('child thread')

obj=Myclass()
t=Thread(target=obj.job)
t.start()

for i in range(10):
    print('main thread')