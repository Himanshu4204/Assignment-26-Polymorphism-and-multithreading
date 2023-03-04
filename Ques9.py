#9. Write a python script to join 2 threads after printing completing the first Question.?
import threading
def multiple(a=None,b=None,c=None):
    if b is not None and c is not None:
        return a*b*c
    elif b is not None:
        return a*b
    else:
        return a

print("Multiples ",multiple(12,6,2))
print("Multiples ",multiple(12,6))

t1=threading.Thread(target=multiple)
t2=threading.Thread(target=multiple)

t1.start()
t2.start()

t1.join()
t2.join()
print("Question First Completed")
