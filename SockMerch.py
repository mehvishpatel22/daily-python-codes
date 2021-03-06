import math
import os
import random
import re
import sys

from collections import Counter

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    n = Counter(ar)
    return sum(i//2 for i in n.values())

n = input()
ar = list(map(int,input().split()))
print(sockMerchant(n,ar))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
