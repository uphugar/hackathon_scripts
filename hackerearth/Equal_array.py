#Equal array

#pass the dictionary
#def ComputeSum(weighted):
    
import sys
import pdb
T=int(input())

for i in range (0,T):   
    N=input()
    lens=input()
    array=[int(n) for n in lens.split(' ')] #lens.split(' ')
    #print (array)
    weighted={}
    val=0
    for i in range(0,len(array)):
        val=val+array[i]
        weighted[i]=val

    maxval=weighted[len(weighted)-1]
    half=int(round(maxval/2))
    Aj=0
    Ajone=0
    for i in range(len(weighted)-1,0,-1):
        #print (weighted[i])
        if(half>=weighted[i]):
            #pdb.set_trace()
            Aj=weighted[i]
            Ajone=weighted[i+1]
            if (half==weighted[i]):
                Aj=weighted[i]
                print (-1)
            else:
                print(Ajone-Aj)
            break
##            if int(N)==4:
##                pdb.set_trace()
                #pdb.set_trace()
            
            #print (Aj)
            break
    
