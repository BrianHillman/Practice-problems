'''
Created on Apr 17, 2012

@author: Brian
'''
def lcm(a,b):
    i = 0
    while i <= a*b:
        i +=a 
        if i%a == 0 and i%b == 0:
            return i
sum = 1;
for x in range(2,20+1):
    sum = lcm(sum,x)
print sum