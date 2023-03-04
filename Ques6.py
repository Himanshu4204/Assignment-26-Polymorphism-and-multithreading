#6. Write a python script to create 5 threads to fill a list with random numbers till 100.?
import threading
import random
num_list = []

def fill_list():
    for i in range(5):
        num_list.append(random.randint(0, 100))

threads = []
for i in range(5):
    t = threading.Thread(target=fill_list)  
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(num_list)
