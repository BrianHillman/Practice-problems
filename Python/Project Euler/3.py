'''
Created on Apr 17, 2012

@author: Brian
'''
def isPrime(num):
    num = abs(num)
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i+=1
    return True
for i in range(int(600851475143**.5),2,-1):
    if isPrime(i) and 600851475143%i -- 0:
        print i
        break
