#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

#
# Complete the 'acmTeam' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY topic as parameter.
#

def acmTeam(topic):
    # Write your code here
    
    res = list(range(0,len(topic)))
    ls = list(itertools.combinations(res,2))

    
    dic = {}
    for i in ls:
        dic[i] = bin(int(topic[i[0]],2) | int(topic[i[1]],2)).count('1')

    print(dic)
    max_score = max(dic.values()) 
    
    result = [key for key,value in dic.items() if value == max_score]
    
    return [max_score,len(result)]
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
