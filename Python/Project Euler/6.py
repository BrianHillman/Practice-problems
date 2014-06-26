'''
Created on Apr 18, 2012

@author: Brian
'''
sumOfSquares = 0
squareOfSums = 0
for x in range(1,101):
    sumOfSquares += x**2
for x in range(1,101):
    squareOfSums += x
squareOfSums = squareOfSums**2
print squareOfSums-sumOfSquares