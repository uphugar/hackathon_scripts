##Bob the bear
import sys
import pdb
N=input()
lens=input()
lengths=[int(n) for n in lens.split(' ')] #lens.split(' ')
t=input()
time=[int(n) for n in t.split(' ')]
#dummy=input()

salmons={}
for i in range(0,len(time)):
    salmons[i]=[lengths[i],time[i]]

times=set(time)
#print(lengths)

##print(salmons)
##print(time)
##print(times)

sorted_x=sorted(salmons.items(), key=lambda salmons: salmons[1][1])

caughttime=[]
sorted_x=sorted(salmons.items(), key=lambda salmons: (salmons[1][1],salmons[1][0]))
j=0
T=0
k=0

j=0

for key, value in sorted_x:
    [le,t]=value
    #print (k,T,key,le,t)
    if(t<=T):
        #print (k)
        if(k<2):
            #print ('second time')
            con1=T-t
            con2=T-t-le
            #print(str(con1)+' ' +str(con2))
            if 0<=T-t and 0>T-t-le:
                caughttime.append([key,T])
                k=k+1
        else:
##            if key==6:
##                pdb.set_trace()
            
            T=T+1
            k=0
            i=0
            while(T-t-i>=0):
                #print ('third time T:'+str(T)+'  t:'+str(t))
                ##compute the between
                con1=T-t
                con2=T-t-le
                #print(str(con1)+' ' +str(con2))
                if 0<=T-t and 0>T-t-le:
                    caughttime.append([key,T])
                    #print('third done')
                    #k=0
                    k=k+1
                    break
                i=i+1
                    
    else:
        #print ('first time')
        k=0
        T=t+1
        i=0
        while(T-t>=0):
            #print(T,t)
            if 0<=T-t and 0>T-t-le:
                con1=T-t
                con2=T-t-le
                #print(str(con1)+' ' +str(con2))
                caughttime.append([key,T])
                k=k+1
                break
            t=t+1
#print (caughttime)
print(len(caughttime))
