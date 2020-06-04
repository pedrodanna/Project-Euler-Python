"""
Created on Thu Jun  4 18:18:55 2020

@author: Pedro Augusto Danna
"""

#Inicialization of the variable that will store the answer value
ans = 0

#Loop that iterates over 0 to 999
for num in range(1000):
    #Checking if a number is multiple by analysing the rest of the division
    if num % 3 == 0 or num % 5 == 0:
        #Summing the numbers that are multiples of 3 or 5
        ans += num
        
#Printing the answer
print(ans)