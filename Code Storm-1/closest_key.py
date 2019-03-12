import sys

temp=input()
data_set={}
i=0
while(i<len(temp)):
    data_set[int(temp[i])]=int(temp[i+1])
    i+=2
ref=raw_input()
refint=int(ref,2)
result=[]

for key, value in data_set.iteritems():
    op= refint ^ value
    count=bin(op).count("0")
    if count<=5:
        result.append(key)

print (str(result)+',').replace(']','').replace('[','').replace(' ','')
