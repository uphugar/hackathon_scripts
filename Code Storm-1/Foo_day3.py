import sys

def Find_t(A,B,C,D,K,left,right):
    while(left<=right):
        t=(left+right)/2
        Ft=Stress(A,B,C,D,t)
        if Ft<=K and (t==right or (Stress(A,B,C,D,t+1)>K)):
            return t
        if Ft>K:
            right=t-1
        elif Ft<K:
            left=t+1
def Stress(a,b,c,d,t):
    return a*t**3+b*t**2+c*t+d

T=input()
i=0
pos_num=[]
res_list=[]
while(i<int(T)):
    vals=raw_input()
    inp=vals.split()
    low=1
    high=1000000
    tim=Find_t(int(inp[0]),int(inp[1]),int(inp[2]),int(inp[3]),int(inp[4]),low,high)
    res_list.append(tim)
    i+=1
    
for it in res_list:
    print it
