#Problem : https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

#!/bin/python3

import os

def stepPerms(n):
    if (n == 1):
        return 1
    elif (n == 2):
        return 2
    elif (n == 3):
        return 4
    else:
        return stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()

    
#Partially solved
