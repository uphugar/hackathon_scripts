import pdb
def passCount(input1, input2, input3):
    dictvals={}
    for j in range(1, input1+1):
        dictvals[j]=0
    i=1
    invL= input1 - input3
    count=0
    nextmax=1
    dictvals[i]=nextmax
    while(nextmax<input2):
        if nextmax%2:# odd
            i=i+invL
            if i>input1:
                i= i - input1
        else:
            i= i + input3
            if i>input1:
                i= i - input1
        dictvals[i]=dictvals[i]+1
        count=count+1
        nextmax=dictvals[i]
    return count

ret=passCount(5,2,3)
print ret