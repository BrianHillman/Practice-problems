'''
Created on Apr 18, 2012

@author: Brian
'''
for a in range(1,334):
    for b in range(1,501):
        for c in range(1,1001/1):
            if a**2 + b**2 == c**2 and a+b+c == 1000:
                print a*b*c