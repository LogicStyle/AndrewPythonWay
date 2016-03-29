#problem 2
import numpy as np
def fib(n):
    if n==1:
        return(1)
    elif n==2:
        return(2)
    else:
        return(fib(n-1)+fib(n-2))
i=1
sum=0
while fib(i)<4e6:
    if fib(i)%2==0:
        sum=sum+fib(i)
        print(i,'and fib',fib(i))
    i=i+1
print(sum)


#problem 3





