#Ben-the gamer
import sys

line1=input()
[N,M]=line1.split(' ')

InMat=[]
#print(N,M)
i=0
dict1={}
while(i<int(N)):
    row_val=[]
    row=input()
    dict1[i]=row
    for it in row:
        row_val.append(it)
    InMat.append(row_val)
    i=i+1

def transpose(mat):
  res_transpose = zip(*mat)
  return res_transpose

#print (InMat)
TransMat=[]
TransMat=transpose(InMat)
#print (str(transpose(InMat)))

weapons={} #weapon no and the weightage of it.
i=0
for row in TransMat:
    weapons[i]=row.count('1') #check ones only. how many times that ith weapon is needed.
    i=i+1

#print (weapons)
i=0
levels={}
for i in range(0, len(InMat)):
    levels[i]=InMat[i].count('1')
    i=i+1

#print (levels)
completed_levels=[]
acquired_weapons=[]
cost=0
for key, value in sorted(levels.items(),key=lambda x: x[1]):
    print (key, value)
    j=0
    k=0
    for j in range(0,len(InMat[key])):
        if InMat[key][j]=='1' and j not in acquired_weapons:
           acquired_weapons.append(j)
           k=k+1
    cost=cost+k*k
    completed_levels.append(key)
    print (acquired_weapons)
    print ('------')

print (cost)
#sorted_d = sorted(levels.items(), key=lambda x: x[1])
# equivalent version
# sorted_d = sorted(d.items(), key=lambda (k,v): v)
