#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'howManyGames' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER d
#  3. INTEGER m
#  4. INTEGER s
#

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    
    if s < p:
        return 0
    res = []
    for i in range(p,m,-d):
        res.append(i)
        if sum(res) == s:
            return len(res)
        if sum(res) > s:
            res.pop()
            return len(res)
        
    if s > sum(res): 
        return len(res) + (s - sum(res))//m

    # result = 0 
    # game_count = 0 
    # while p <= s: 
    #     if p + (p - d) > s:
    #         break 
    #     elif p > m:
    #         game_count += 1 
    #         p = p - d 
    #     else : 
    #         game_count += 1 
    #         p = p - m 
        
    # return game_count 
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
