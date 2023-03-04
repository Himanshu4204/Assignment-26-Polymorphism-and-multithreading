#7. Write a python script to create a clock where 1st thread will print the current time every second 
#    and 2nd will print “1 Minute Completed” after every 1 minute.?
import time
from threading import Thread
def second():
    while True:
        current_time = time.strftime("%H:%M:%S", time.localtime())
        print(current_time)
        time.sleep(1)

def minute():
    while True:
        time.sleep(60)     
        print("1 Minute Completed")

t1=Thread(target=second)
t2=Thread(target=minute)
t1.start()
t2.start()

t1.join()
t2.join()

