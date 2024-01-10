#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    
    i = 0
    res = 100 
    n = len(c)
    
    #k = k if n % k == 0 else math.gcd(n, k)
    #print(k_res)
    
    while True:
        i = (i+k)%n
        
        if c[i] == 1:
            res -= 3 
        else:
            res -=1 
        
        if i == 0:
            break
    
    return res
        

    
    # while i != 0:
    #     print(res)
    #     print('First i:',i)
    #     if c[i] == 1:
    #         res -= 2 
    #         print(i,c[i],res)
    #     i = (i + k)%n
    #     #print('Last i:',i)
    #     res -= 1 
    #     #print('res ',res)
        
    # if c[0] == 1:
    #     res -= 2
        
    # print(res)
    # return res
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    fptr.write(str(result) + '\n')

    fptr.close()
