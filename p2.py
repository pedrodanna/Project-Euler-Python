"""
Created on Fri Jun  5 17:14:05 2020

@author: Pedro Augusto Danna
"""

#Inicialization of the variable that will store the answer value
ans = 0

#Inicialization of the Fibonacci sequece
x = 1
y = 1

#Loop over the range where the Fibonacci  number values don't exceed 4M
for n in range(1,33):
    #Calculation of the next number of Fibocci sequence
    z = y + x
    
    #Checking if the number is even
    if z % 2 == 0:
        #Summing the numbers that are even
        ans += z
    
    #Updating the sequence
    x = y
    y = z
        
#Printing the answer    
print(ans)
    