import sys
import os
'''Complete the function below.'''


def FindingMoves(input1):
    n=input1+3
    if input1==1:
        n=4
    else if input1=2:
        n=5
    return (n*(n+1)*(2*n+1))/6-1-5

ip1 = int(raw_input());
output = FindingMoves(ip1)
print(str(output))
