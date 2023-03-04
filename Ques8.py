#8. Write a python script to change the name of the Thread.?
import threading 
def my_func():
    print(f"Thread name is {threading.current_thread().name}")

# create a thread and set its name
my_thread = threading.Thread(target=my_func, name="MyThread")

my_thread.start()
my_thread.name = "NewThreadName"
my_thread.join()
