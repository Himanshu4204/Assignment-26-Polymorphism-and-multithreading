#Write a python script to create 2 threads to add all the values from 1 to 100.?
from threading import Thread

def add_numbers(start,end):
    result=0
    for i in range(start,end+1):
        result+=i
    print(f"Sum of {start}to{end} is :{result}")

t1=Thread(target=add_numbers,args=(1,50))
t2=Thread(target=add_numbers,args=(51,100))

t1.start()
t2.start()

t1.join()
t2.join()

print('Task Completed')
