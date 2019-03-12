import sys
from fractions import gcd
n=input()
count=0
res_list=[]
while(count<int(n)):
    no_of_gcd=1
    val_list=[]
    val_list=raw_input()
    ab=val_list.split()
    A=int(ab[0])
    B=int(ab[1])
    i=1
    while(i<=A):
        j=1
        while(j<=B):
            if i==j:
                pass
            elif gcd(i,j)==1:
                no_of_gcd+=1
            
            j+=1
        i+=1
    res_list.append(no_of_gcd)
    no_of_gcd=1
    count+=1

for item in res_list:
    print item
