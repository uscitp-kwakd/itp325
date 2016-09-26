from math import sqrt

num=1
pcnt=0

def is_it_prime(number):
    sqroot=int(sqrt(number))
    i=2
    while i<=sqroot:
        if number%i==0:
            return False
        i=i+1
    return True

num = int(input("Enter a number: "))
primeFinder = num

while(1):
    num=num+1
    if is_it_prime(num):
        pcnt=pcnt+1
    if pcnt==primeFinder:
        print 'The',pcnt,'th prime is',num
        break
 