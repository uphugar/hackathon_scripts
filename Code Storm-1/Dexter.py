import sys
import pdb

##def checkplus(Matrix,row,col,rowlength,collength):
##    plus=0
##    counta=0
##    countb=0
##    templist=[]
##    templist.append(Matrix[row][col])
##    stra='a'
##    strb='b'
##    k=1
##    while(row+k<rowlength and row-k>=0 and col-k>=0 and col+k<collength):
##        templist.append(Matrix[row-k][col])
##        templist.append(Matrix[row][col-k])
##        templist.append(Matrix[row+k][col])
##        templist.append(Matrix[row][col+k])
##        counta=templist.count(stra)
##        countb=templist.count(strb)     
##        if countb<2 and counta>1 :
##            plus=plus+1
##        elif counta<2 and countb>1:
##            plus=plus+1
##        else:
##            return plus
##        i=i+1
##    return plus

stra='a'
strb='b'       
T=input()
for h in range(0,T):
    NM=raw_input()
    N,M=NM.split()
    N=int(N)
    M=int(M)
    Matrix=[]
    for j in range(0,N):
        rowinput=raw_input()
        Matrix.append(rowinput)

    plus=0
    #pdb.set_trace()
    for i in range(N-2,0,-1):
        for j in range(M-2,0,-1):
            #count=count+checkplus(Matrix,i,j,N,M)
            counta=0
            countb=0
            templist=[]
            templist.append(Matrix[i][j])
            k=1
            while(i+k<N and i-k>=0 and j-k>=0 and j+k<M):
                templist.append(Matrix[i-k][j])
                templist.append(Matrix[i][j-k])
                templist.append(Matrix[i+k][j])
                templist.append(Matrix[i][j+k])
                counta=templist.count(stra)
                countb=templist.count(strb)     
                if countb<2 and counta>1 :
                    plus=plus+1
                elif counta<2 and countb>1:
                    plus=plus+1
                else:
                    break
                k=k+1
            
    print plus
