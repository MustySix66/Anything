#	Submissions	Leaderboard	Discussions	Editorial
# You are given a spreadsheet that contains a list of N athletes and their details 
# (such as age, height, weight and so on). You are required to sort the data based 
# on the Kth attribute and print the final resulting table. 


        #!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    numAtletas = int(first_multiple_input[0])
    ## m = int(first_multiple_input[1])
    arr = []
    for _ in range(numAtletas):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input().strip())

    # Sort the array based on the kth attribute
    arr.sort(key=lambda x: x[k])
    # Print the final resulting table
    for row in arr:
        print(' '.join(map(str, row)))
