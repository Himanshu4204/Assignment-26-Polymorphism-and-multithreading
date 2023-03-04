#4. Write a python script to create two Threads. First thread will print all Even numbers
#    and Second thread will print all Odd numbers till 100.
from threading import Thread
from time import sleep

def Even_numbers():
    for i in range(1,101):
        print("Even Numbers :",i)

def Odd_numbers():
    for i in range(1,101,2):
        print("Odd Numbers :",i)
        sleep(1)

t1=Thread(target=Even_numbers)
t2=Thread(target=Odd_numbers)

t1.start()
t2.start()

t1.join()
t2.join()
print("Done")

