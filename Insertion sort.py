#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    result_arr = []
    res = arr[-1]
    for i in range(n-1,0,-1):
        if arr[i-1] > res:
            arr[i] = arr[i-1]
            print(*arr)
            if i == 1: 
                arr[i-1] = res 
                print(*arr)
                break
        else:
            arr[i] = res
            print(*arr)
            break
    # print(arr)
    # print(result_arr)
    #return result_arr
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
