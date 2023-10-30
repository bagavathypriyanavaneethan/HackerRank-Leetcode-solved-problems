#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort2' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort2(n, arr):
    # Write your code here
    for i in range(0,n-1):
        if arr[i+1] > arr[i]:
            print(*arr)
            continue 
        else: 
            for j in range(0,i+1):
                if arr[j] < arr[i+1] and arr[i+1] < arr[j+1]:
                    temp = arr.pop(i+1)
                    arr.insert(j+1,temp)
                    print(*arr)
                elif arr[j] > arr[i+1]:
                    temp = arr.pop(i+1)
                    arr.insert(j,temp)
                    print(*arr)
                    
    
    # print(arr)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
