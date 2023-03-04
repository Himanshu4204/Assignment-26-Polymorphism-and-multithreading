# 10. Write a python script to check whether a given number is prime or armstrong number using 2 different threads.?
import threading
num=int(input("Enter a Number :"))
def is_armstrong(num):
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    return num==sum

def is_prime(num):
    for i in range(2,num):
        if num%i==0:
           return False
    return True
  
t2=threading.Thread(target=lambda: print(f"{num} is Armstrong Number" if is_armstrong(num) else f"{num} is Not Armstrong Number"))
t1=threading.Thread(target=lambda: print(f"{num} is Prime Number" if is_prime(num) else f"{num} is Not prime Number"))

t1.start()
t2.start()

t1.join()
t2.join()
print("Task Completed")



