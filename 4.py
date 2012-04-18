'''
Created on Apr 17, 2012

@author: Brian
'''
def isPalindrome(num):
    num = str(num)
    for i in range(0,int(len(num)/2)):
        if(num[i] == num[len(num)-i-1]):
            pass
        else:
            return False
    return True
for x in range(999*999,0,-1):
    if isPalindrome(x):
        print x
        break
    