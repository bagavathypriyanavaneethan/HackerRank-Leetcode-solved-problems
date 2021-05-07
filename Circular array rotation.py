#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'circularArrayRotation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER k
#  3. INTEGER_ARRAY queries
#

def circularArrayRotation(a, k, queries):
    # Write your code here
    '''arr=[]
    for i in range(0,k):
        if i == 0:
            arr[0] = [a[-1]]
        else:
            arr[0] = [arr[-1]]
        for j in range(0,len(a)):
            arr.append(a[j])
    print(arr)
    for i in queries:
        return arr[i]'''
    k = k%len(a)
    arr = []
    for i in range(len(a)-k,len(a)):
        #print(i)
        arr.append(a[i])
    print(arr)
    for i in range(0,len(a)-k):
        arr.append(a[i])
    print(arr)
    return [arr[i] for i in queries]
    '''k = k%len(a)
    a= a[-k:] + a[:-k]
    return [a[i] for i in queries]'''

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
