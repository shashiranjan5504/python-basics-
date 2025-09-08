from threading import *
from time import sleep
class hello (Thread):
    def manish(self):
        for i in range(20):
            print("hello")
            sleep(1)
    def  run(self):
        return self.manish()
class hi(Thread):
    def manish(self):
        for i in range(20):
            print("hi")
            sleep(1)
    def run(self):
        return self.manish()
t1=hello()
t2=hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")