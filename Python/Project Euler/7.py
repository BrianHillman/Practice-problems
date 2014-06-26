'''
Created on Apr 18, 2012

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
count = 0
num = 0
while count <= 10000:
    num += 1
    if isPrime(num):
        count +=1
print num