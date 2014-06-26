'''
Created on Apr 17, 2012

@author: Brian
'''
sum = 0
prev1 = 1
prev2 = 2
while prev2 <= 4000000:
    if prev2 % 2 == 0:
        sum += prev2
    prev1,prev2 = prev2,prev2+prev1
print sum
