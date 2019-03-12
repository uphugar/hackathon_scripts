import math
import pdb
line1=input()

N,C=line1.split(' ') #lens.split(' ')
N=int(N)
C=int(float(C))

#print (N,C)
i=0
Mat=[] #[xi,yi,mi,ti]
while (i<N):
    line1=[int(n) for n in input().split(' ')]
    Mat.append(line1)
    i=i+1

#print (Mat)
OnlyRx=[i for i in Mat if (i[2]>i[3])]

#print(OnlyRx)
tree=[]
flag=True

if (len(OnlyRx)>1):
    print ('only Rx')
else:
    for j in range(0,N):
        #if (j==1):
            #pdb.set_trace()
            #print(1)
        for k in range(0,N):
            if (j!=k):
                xa,ya,ma,ta=Mat[k]
                xb,yb,mb,tb=Mat[j]
                dab=math.sqrt((xb-xa)**2+(yb-ya)**2)
                if dab<C and ma<ta:
                    #tree.append(Mat)
                    continue
                else:
                    flag=False
                    break
        if flag:
            tree.append(j)

if (len(tree)>0):
    #print (tree)
    print (' '.join([str(item) for item in tree]))
else:
    print (-1)
