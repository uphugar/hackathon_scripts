import sys
import os

def nochange_bits(input1,input2,input3):
    if input2<=0 or input3<=0:
        return -1
    count=len(input1)-1
    count1=count-input2
    count2=count-input3
    return min(count1,count2)

try:
    ip1 = raw_input()
except:
    ip1 = None
ip2 = int(raw_input());
ip3 = int(raw_input());
output = nochange_bits(ip1,ip2,ip3)
print(str(output))
