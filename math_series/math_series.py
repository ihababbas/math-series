import pytest
 ## Recursive Solution
 # 0, 1, 1, 2, 3, 5, 8, 13, 21 ,34 ,55,89,144,233,377,610   fibonacci
# 2, 1, 3, 4, 7, 11, 18, 29, 47,76,123,199,322,521,843,1364    lucas 
def Fibonacci(n): 
    if n<0: 
        # the first input must be 0
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
   
  

 ## Recursive Solution 

def lucas(n) : 
      
    # Base cases  
    if (n == 0) : 
        return 2
    if (n == 1) : 
        return 1
  
    # the  relation  
    return lucas(n - 1) + lucas(n - 2)





def sum_series(n, first=0, second=1):
    #Determine nth number in series 
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return sum_series(n - 1, first, second) + sum_series(n - 2, first, second)

    