#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    
    res = ''
    k = k%26
    for i in s:
        
        #For alphabets out of range
        if i.isalpha() and (ord(i.lower()) + k) not in range(ord('a'),ord('z')+1):
            if i.islower():
                temp = ( (ord(i) + k) - ord('z') + ord('a') - 1)
                res = res + chr(temp)
            elif i.isupper():
                temp = ( (ord(i) + k) - ord('Z') + ord('A') - 1)
                res = res + chr(temp)
                
        
        # For alphabets 
        elif ord(i.lower()) in range(ord('a'),ord('z')+1):
            res = res + (chr(ord(i) + k))
        
        # For special characters
        else: 
            res = res + i 
            print()
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
