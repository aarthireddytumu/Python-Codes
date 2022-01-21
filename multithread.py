# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 09:15:17 2021

@author: aarthi.reddy.tumu
"""

#from threading import *
#from time import sleep
#class Hello(Thread):
#    def run(self):
#        for i in range(5):
#            print("Hello")
#            sleep(1)
#class Hi(Thread):
#    def run(self):
#        for i in range(5):
#            print("Hi")
#            sleep(1)
#t1=Hello()
#t2 = Hi()
#t1.start()
#sleep(0.2)
#t2.start()
#t1.join()
#t2.join()
#print("bye")


import threading # locks- synchronisation tool
#locked/unlocked
#acquire()/release()
from time import sleep
lock = threading.Lock()
deposit = 100 # resource
def add_profit():
    global deposit
    for i in range(10000000):
        lock.acquire()
        deposit +=10
        lock.release()
def pay_bill():
    global deposit
    for i in range(10000000):
        lock.acquire()
        deposit -=10
        lock.release()
t1 = threading.Thread(target = add_profit,args=())
t2 = threading.Thread(target = pay_bill,args=())
t1.start()
t2.start()
t1.join()
t2.join()
print(deposit)



